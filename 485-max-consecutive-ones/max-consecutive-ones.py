class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
     

        # left = 0
        # res = 0

        # for right in range(len(nums)):  two pointer sliding window solution 
        #     if nums[right]==0:
        #         left = right+1

        #     res = max(res, right - left +1)

        # return res

        count = 0
        res = 0
        for num in nums:
            if num == 1:    #normal solution but littel better
                count+=1
            else:
                count =0


            res = max(res, count)

        return res
        