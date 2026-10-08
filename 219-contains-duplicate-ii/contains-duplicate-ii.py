class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen= {}
        for i in range(len(nums)):
            if nums[i] in seen and abs(i-seen[nums[i]]) <= k:
                return True

            seen[nums[i]] = i #Put the current number as the KEY, and its current index as the VALUE.like nums[i] will be key and i will be the value
            
        return False