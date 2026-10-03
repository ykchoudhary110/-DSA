class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 1
        high = 0
        while low<len(nums):
            if nums[low]!=nums[high]:
                high+=1
                nums[high] = nums[low]
            else:
                low+=1
        return high+1



        # low =1
        # high=0
        # while low<len(nums):
        #     if nums[low]!= nums[high]:
        #         high+=1
                
        #         nums[high]=nums[low]
            
        #     low+=1
        # return high + 1
