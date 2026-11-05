class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        # pairs = {'(': ')', '{': '}', '[' : ']'} never do like this as it will create error becaseu

        for char in s:
            if char in pairs:
                if len(stack)>0 and stack[-1]==pairs[char]:
                            #     stack[-1]#this is top element 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack)==0:
            return True
        else:
            return False
        

        