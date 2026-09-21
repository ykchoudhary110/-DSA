class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        res = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros+=1
            

            while zeros>1:                     
                if nums[left]==0:                 
                    zeros-=1
                left+=1

            res = max(res,right-left)

        return res
#     1. Add right element
#        ↓
# 2. Check zeros
#        ↓
# 3. Too many zeros?
#        ↓
# 4. Shrink using left
#        ↓
# 5. Window is valid
#        ↓
# 6. Calculate answer