class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        left = 0
        res = []
        sum = 0
        for right in range(len(nums)):
            sum+=nums[right]
            res.append(sum)

        return res

    
        