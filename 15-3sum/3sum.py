from typing import List #higly important
# here
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = n-1
            
            while left<right:
                total= nums[left]+nums[right]+nums[i]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res
                
        





        # nums.sort()
        # n = len(nums)
        # res = []

        # for i in range(n-2):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue

        #     left = i+1
        #     right = n-1

        #     target = -1 * nums[i]

        #     while left<right:
        #         s = nums[left] + nums[right]

        #         if s==target:
        #             res.append([nums[i], nums[left],nums[right]])

        #             left+=1
        #             right-=1

        #             while left<right and nums[left] == nums[left-1]:
        #                 left+=1
        #             while left<right and nums[right] == nums[right+1]:
        #                 right-=1

        #         elif s<target:
        #             left+=1
                    
        #         else:
        #             right-=1
        # return res


     