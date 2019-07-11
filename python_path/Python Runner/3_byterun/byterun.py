# -*- coding:utf-8 -*-
import collections
import operator
import dis
import sys
import types
import inspect


Block =collections.namedtuple("Block","type","handler","stack_height")
class VirtualMachineError(Exception):
    pass


class VirtualMachine(object):
    BINARY_OPERATORS={
        'POWER':pow,
        'MULTIPLY':operator.mul,
        'FLOOR_DIVIDE':operator.floordiv,
        'TRUE_DIVIDE':operator.truediv,
        "MODULO":operator.mod
        'ADD': operator.add,
        'SUBTRACT':operator.sub,
        'SUBSCR':operator.getitem,
        'LSHIFT':operator.lshift,
        'RSHIFT':operator.rshift,
        'AND':operator.and_,
        'OR':operator.or_,
        'XOR':operator.xor
    }
    def __init__(self):
        # call stack
        self.frames = []
        # current frame
        self.frame = None
        # frame return value
        self.return_value = None
        self.last_exception = None

    def run_code(self, code, global_names=None, local_names=None):
        """ entrance of running python program,
        code: compiled code -> code_obj
        create a new frame from input code_obj
        """
        frame = self.make_frame(
            code, global_names=global_names, local_names=local_names)
        self.run_frame(frame)

    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        """ create a new frame
        code: code obj
        callargs: params when the function called
        """
        if global_names is not None:
            global_names = global_names
            if local_names is None:
                local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = {}
        else:
            global_names = local_names = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
                '__package__': None
            }
        # save callargs to local varibale space
        local_names.updae(callargs)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame

    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None

    def run_frame(self, frame):
        self.push_frame(frame)
        while True:
            byte_name,arguments=self.parse_byte_and_args()
            why=self.dispatch(byte_name,arguments)
            while why and frame.block_stack:
                why=self.manage_block_stack(why)
            if why:
                break
        self.pop_frame()
        if why=="exception":
            exc,val,tb=self.last_exception
            e=exc(val)
            e.__traceback__=tb
            raise e
        return self.return_value


    def top(self):
        return self.frame.stack[-1]
    def pop(self):
        return self.frame.stack.pop()
    def push (self,*vals):
        self.frame.stack.extend(vals)
    def popn(self,n):
        if n:
            ret=self.frame.stack[-n:]
            self.frame.stack[-n:]=[]
            return ret
        else:
            return []
    def parse_byte_and_args(self):
        f=self.frame
        opoffset=f.last_instruction
        # get the operation will be execute
        byte_code=ord(f.code_obj.co_code[opoffset])
        f.last_instruction+=1
        byte_name=dis.opname[byte_code]

        # if this opt don't have arg
        if byte_code >= dis.HAVE_ARGUMENT:
            arg=f.code_obj.co_code[f.last_instruction:f.last_instruction+2]
            f.last_instruction+=2
            arg_val = ord(arg[0]) +(ord(arg[1])*256)
            if byte_code in dis.hasconst: # find consts
                arg=f.code_obj.co_consts[arg_val]
            elif byte_code in dis.hasname:# find var names
                arg = f.code_obj.co_name[arg_val]
            elif byte_code in dis.haslocal:# find local var names
                arg=f.code_obj.co_varnames[arg_val]
            elif byte_code in dis.hasjrel:# calc jmp address
                arg=f.last_instruction+arg_val
            else :
                arg=arg_val
            argument = [arg]
        else:
            argument = []
        return byte_name,argument
    def dispatch(self,byte_name,argument):
        why=None
        try:
            bytecode_fn=getattr(self,"byte_%s" % byte_name,None)
            if bytecode_fn is None:
                # sperate one opt var , two opt var and other
                if byte_name.startswith('UNARY_'):
                    self.unary_operator(byte_name[6:])
                elif byte_name.startswith("BINARY_"):
                    self.binary_operator(byte_name[7:])
                else:
                    raise VirtualMachineError("unsupported bytecode type: %s" % byte_name)
            else:
                why=bytecode_fn(*argument)
        except:
            self.last_exception=sys.exc_info()[:2]+(None,)
            why="exception"
        return why

    
    def unary_operator(self,op):

        pass
    def binary_operator(self,op):
        x,y=self.popn(2)
        self.push(self.BINARY_OPERATORS[op](x,y))
        pass
    
    def push_block(self,b_type,handler=None):
        stack_height=len(self.frame.stack)
        self.frame.block_stack.append(Block(b_type,handler,stack_height))
    def pop_block(self):
        return self.frame.block_stack.pop()
    def unwind_block(self,block):
        """unwind the values on the data stack corresponding to a given block"""
        if block.type=="except-handler":
            # the exception it self is on the stack as type,value and traceback
            offset=3
        else:
            offset=0
        while len(self.frame.stack)>block.stack_height+offset:
            self.pop()
        if block.type=="except-handler":
            traceback,value,exctype=self.popn(3)
            self.last_exception=exctype,value,traceback
    def manage_block_stack(self,why):
        """manage block stack for a frame ,operate the circle,execption process and return  of block stack and data stack"""
        frame=self.frame
        block =frame.block_stack[-1]
        if block.type =="loop" and why == "continue":
            self.jump(self.return_value)
            why=None
            return why
        self.pop_block()
        self.unwind_block(block)
        if block.type=="loop" and why=="break":
            if (block.type in ["setup-except","finally"] and why=="exception"):
                self.push_block('except-handler')
                exctype,value,tb=self.last_exception
                self.push(tb,value,exctype)
                # TODO why twice??
                self.push(tb,value,exctype)
                why = None
                self.jump(block.handler)
                return why
            elif block.type=="finally":
                if why in ("return","continue"):
                    self.push(self.return_value)
                    self.push(why)
                    why=None
                    self.jump(block.handler)
                    return why
            return why
    # stack manipulation
    def byte_LOAD_CONST(self,const):
        self.push(const)
    def byte_POP_TOP(self):
        self.pop()
    
    # Names
    def byte_LOAD_NAME(self.name):
        frame=self.frame
        if name in frame.f_locals:
            val=frame.f_locals[name]
        elif name in frame.f_globals:
            val=frame.f_globals[name]
        elif name in frame.f_builtins:
            val=frame.f_builtins[name]
        else:
            raise NameError("name '%s' is not defined" % name)
        self.push(val)
    def byte_STORE_NAME(self,name):
        self.frame.f_locals[name]=self.pop()
    def byte_LOAD_FAST(self,name):
        if name in self.frame.f_locals:
            val=self.frame.f_locals[name]
        else:
            raise UnboundLocalError(
                "local variable '%s' referenced before assignment " % name
            )

        self.push(val)
    def byte_STORE_FAST(self,name):
        self.frame.f_locals[name]=self.pop()
    def byte_LOAD_GLOBAL(self,name):
        f=self.frame
        if name in f.f_global:
            val=f.f_globals[name]
        elif name in f.builtins:
            val=f.builtins[name]
        else:
            raise NameError(
                "global name '%s' is not defined" % name
            )
        self.push(val)
class Frame(object):
    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.f_globals = global_names
        self.f_locals = local_names
        self.prev_frame = prev_frame
        # data stack
        self.stack = []
        # block stack
        self.block_stack = []

        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names["__builtins__"]
            if hasattr(self.builtin_names, '__dict__'):
                self.builtin_names = self.builtin_names.__dict__
        # the last instruction
        self.last_instruction = 0


class Function(object):
    __slots__ = [
        "func_code", 'func_name', 'func_defaults', 'func_locals', 'func_dict', 'func_closure', '__name__', '__dict__', '__doc__', '_vm', '_func'
    ]

    def __init__(self, name, code, globs, defaults, closure, vm):
        self._vm = vm
        self.func_code = code
        # function name will store at code.co_name
        self.func_name = self.__name__ = name or code.co_name
        # default values for parameters
        self.func_defaults = tuple(defaults)
        self.func_globals = globs
        self.func_locals = self._vm.frame.f_locals
        self.__dict__ = {}
        # closure informations of function
        self.func_closure = closure
        self.__doc__ = code.co_consts[0] if code.co_consts else None

        # sometimes we will using real python's function
        kw = {
            'argdefs': self.func_defaults,
        }
        # create cell object for closure
        if closure:
            kw['closure'] = tuple(make_cell(0) for _ in closure)
        self._func = types.FunctionType(code)

    def __call__(self, *args, **kwargs):
        """Create a frame and run when call"""
        # get function args using inspect
        callargs = inspect.getcallargs(self._func, *args, **kwargs)
        # create frame of function
        frame = self._vm.make_frame(
            self.func_code, callargs, self.func_globals, {}
        )
        return self._vm.run_frame(frame)


def make_cell(value):
    """create a real cell"""
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]