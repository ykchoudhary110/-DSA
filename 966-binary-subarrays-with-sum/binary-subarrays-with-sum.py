class Solution:

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            left =0 
            total =0
            res = 0

            for right in range(len(nums)):
                total += nums[right]
                #if condiotn is false
                while total>k:
                    total -= nums[left]
                    left+=1

                res += right-left+1
            return res
        return (atmost(goal) - atmost(goal-1)) # so basically atlmost find all the subarray coutn ahving sum goal or less than goal so lest subract goal -1 sum to bring all subarray count exactly equal to goal
            

        