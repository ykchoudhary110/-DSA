class Solution:
    def findMin(self, nums: list[int]) -> int:
        nums.sort()
        return nums[0]
        # left = 0
        # right = len(nums)-1
        # while left<right:
        #     mid= (left+right)//2
        #     if nums[mid]>nums[right]:
        #         left = mid+1
        #     else:
        #         right = mid # as mid can be the lowest elemtn

        # return nums[left] # at the end left and right will share the same element rest left will have lowest element
       
      
        

        # left = 0
        # right = len(nums)-1

        # while left<right:
        #     mid = (left+right)//2
        #     if nums[mid]>nums[right]:
        #         left = mid+1
        #     else:
        #         right = mid
        # return nums[left]









        # # nums.sort()   #easy one

        # # return nums[0]
        