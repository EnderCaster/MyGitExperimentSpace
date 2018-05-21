class Solution:
    def reverse_words_in_string(self, origin):
        if len(origin)<=0:
            return origin

        s_ret,s_temp=list(),list()
        ix=len(origin)
        while(ix!=0):
            s_temp=list()
            print(ix)
            while origin[ix-1:ix]!=" " and origin[ix-1:ix]!="":
                s_temp.append(origin[ix-1:ix])
                if ix==0:
                    break
                print(origin[ix:ix+1])
                
            if len(s_temp)!=0:
                if len(s_ret)!=0:
                    s_ret.append(' ')

                s_temp.reverse()
                s_ret.append(s_temp)
            

        return s_ret

test_class=Solution()
result=test_class.reverse_words_in_string("hello world")
print(result)