what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),
                     ("LOAD_VALUE", 1),
                     ("ADD_TWO_VALUES", None),
                     ("LOAD_VALUE", 2),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5,8]
}


class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num+second_num
        self.stack.append(total)

    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']
        numbers = what_to_execute['numbers']

        for each_step in instructions:
            instruction, argument = each_step
            rf = getattr(self, instruction)
            if argument is not None:
                rf(numbers[argument])
            else:
                rf()


if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.run_code(what_to_execute)
