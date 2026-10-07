class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        left = 0
        freq= {}
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right],0)+1

            if freq[nums[right]]>len(nums)//2:
                return nums[right]


