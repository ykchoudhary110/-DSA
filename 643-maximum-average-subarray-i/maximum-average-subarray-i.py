class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:



        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
            
        return max_sum/k

        # # left=0
        # # res=0
        # window_sum = sum(nums[:k])
        # max_sum = window_sum

        # for i in range(k, len(nums)): # since we have already sum of first k elements outside the loop previously so that why we need to start from the k 
        #     window_sum += nums[i]-nums[i-k]   # i-k means whe element exiting the window is the i - k end (exp - if i is at 4 and k is also 4 then 4-4 is 0 so element exiting is the nums[0])
        #     max_sum=max(max_sum, window_sum)

        # return max_sum/k

        