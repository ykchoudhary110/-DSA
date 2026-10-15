class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        left_sum = 0
        total = sum(nums)
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i] # total = left_sum + right_sum +nums[i]
            
            if left_sum == right_sum:
                return i
            left_sum+=nums[i]
        return -1