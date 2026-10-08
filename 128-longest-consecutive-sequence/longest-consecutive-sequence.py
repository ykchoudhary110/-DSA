class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums) # as finding element in set takes o(1) tc soit is easier ot solve this 
        longest = 0
        for num in seen:
            if num - 1 not in seen:   # Start counting only if this is the first number of a sequence
                length=1 # this condition says that form here the our consecutive list will start
                while num+length in seen: # Keep checking the next consecutive number
                    length+=1
                
                longest = max(length, longest)
        return longest

        