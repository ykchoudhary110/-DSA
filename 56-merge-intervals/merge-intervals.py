class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = []
        for current in intervals:
            if len(merged)==0 or current[0]>merged[-1][1]:
                merged.append(current)
            else:
                merged[-1][1]= max(merged[-1][1], current[1])
        return merged