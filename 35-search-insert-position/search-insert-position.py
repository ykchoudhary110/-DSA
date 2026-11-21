class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right  = len(nums)-1
        while left<=right:# nums [1] adn target = 2 so nums has not 2 so it need to be inserted at 2 so first condtion says left = 0
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return left # the entire window is shrink to the left of the this 