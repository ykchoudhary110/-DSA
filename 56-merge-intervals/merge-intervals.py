class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = []
        # for current in intervals:
        #     if len(merged)==0 or current[0]>merged[-1][1]:
        #         merged.append(current)
        #     else:
        #         merged[-1][1]= max(merged[-1][1], current[1])
        # return merged

        #insted of thsi for what we can do it for better understanding is 
        for start , end in intervals:
            if len(merged)==0 or start>merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1]=max(merged[-1][1], end)
        return merged