class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(','}':'{',']':'['}
        for char in s:
            if char in pairs:
                if len(stack)>0 and stack[-1]==pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack)==0:
            return True
        else:
            return False


        # stack = []
        # pairs = {')': '(', '}': '{', ']': '['}#when in if 3 condition when it check for in it goes by deafault to thet key and then matches it withe current one and add to the stack so need to think to add key as closing blackets
        # # pairs = {'(': ')', '{': '}', '[' : ']'}  # PYTHON RULE: 'char in pairs' ONLY checks the LEFT side (the keys).
        # # We put CLOSING brackets on the left so we can detect them easily!
        # for char in s:
        #     if char in pairs:
        #         if len(stack)>0 and stack[-1]==pairs[char]:
        #                     #     stack[-1]#this is top element 
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)
        # if len(stack)==0:
        #     return True
        # else:
        #     return False




        
        

        