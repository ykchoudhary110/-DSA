class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def built(text):
            stack = []
            for char in text:
                if char!='#':
                    stack.append(char)
                elif len(stack)>0:
                    stack.pop()

            return stack
        return built(s)==built(t)