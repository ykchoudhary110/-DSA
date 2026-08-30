class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        mindiff = float("inf")
        closest = 0

        for i in range(n-2):
            left = i+1
            right = n-1

            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                diff = abs(sum - target)

                if diff<mindiff:
                    mindiff = diff
                    closest = sum
                
                if sum==target:
                    return sum
                elif sum<target:
                    left+=1
                else:
                    right-=1

        return closest

        