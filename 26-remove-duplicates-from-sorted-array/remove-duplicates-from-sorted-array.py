class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        high = 0
        low = 1
        while low < len(nums):
            if nums[low] != nums[high]:
                high += 1
                nums[high] = nums[low]
            low += 1
        return high + 1
        