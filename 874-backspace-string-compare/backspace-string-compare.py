class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def built(string):
            stack = []
            for char in string:
                if char!='#':
                    stack.append(char)
                elif len(stack)>0:
                    stack.pop()

            return stack
        return built(s)==built(t)