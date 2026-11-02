
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid= (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left= mid+1

            else:
                if nums[mid]<target<=nums[right]:
                    left= mid+1
                else:
                    right= mid-1
        return -1

            
















        left = 0
        right = len(nums) - 1

        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # If middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # Check if the LEFT half is sorted
            if nums[mid] >= nums[left]: # we use "=" when the boundary values shoudl be there to consider in this entire code

                # Check if target lies in the left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, the RIGHT half is sorted
            else:

                # Check if target lies in the right sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target does not exist
        return -1
