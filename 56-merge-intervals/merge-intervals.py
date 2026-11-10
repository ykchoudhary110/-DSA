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
        #unpackign the elements in the interval adn this is common in python this way
        for start , end in intervals:
            if len(merged)==0 or start>merged[-1][1]: # Case A: If merged is empty, OR this interval starts AFTER the previous ended:
            # (No overlap, so add it as a new separate interval)
                merged.append([start, end])
            else:  # Case B: They OVERLAP!
            # (Update the end time of the previous interval to whichever is larger)
                merged[-1][1]=max(merged[-1][1], end)
        return merged