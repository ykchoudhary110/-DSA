class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right  = len(nums)-1
        while left<=right:# suppose if left and right has 0 so 0<0 = false so alwasy here 0<=0
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return left # the entire window is shrink to the left of the this 