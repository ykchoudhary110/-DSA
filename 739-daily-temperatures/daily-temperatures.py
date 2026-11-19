class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0]*n # because it creases array res with size n and all elemtnet is 0 by deafulat so if we didn't find any warmer day for anyone then simply it zero
        stack = []
        for current_day, current_temp in enumerate(temperatures):# enumerate does both check stores index and values
            while len(stack)>0 and current_temp>temperatures[stack[-1]]: # becuase stack sotores day and not the tempreature so we have to call in this way
                prev_day = stack.pop() # prev day varable is the the one which is poped form the top
                res[prev_day] = current_day - prev_day # now change res{prev_day value} with the diffrence of curret and prev
            stack.append(current_day)
        return res
        