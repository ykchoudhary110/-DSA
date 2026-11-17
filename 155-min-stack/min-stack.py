class MinStack:

    def __init__(self): #so we are creating two stack stack and min stack adn use self to keep it alive
        self.stack = []# self will store this stack even if other fuciton is ended its work
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min_stack)==0:
            self.min_stack.append(value)
        else:
            current_min = self.min_stack[-1]
            if current_min>value:
                self.min_stack.append(value)
            else:
                self.min_stack.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()