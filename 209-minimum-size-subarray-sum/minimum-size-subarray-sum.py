class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        low = 0
        
        window_sum = 0
        min_len = float("inf")

        for high in range(0, n):
            window_sum += nums[high]

            while window_sum>=target:
                min_len = min(min_len, high-low+1)
                window_sum -= nums[low]
                low += 1
        return 0 if min_len== float("inf") else min_len
            


        