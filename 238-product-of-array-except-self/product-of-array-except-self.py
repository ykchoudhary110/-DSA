class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        left_product = 1
        right_product = 1
        n =len(nums)
        for i in range(n):
            ans.append(left_product)
            left_product = left_product*nums[i]
        for i in range(n-1, -1, -1):
            ans[i]= ans[i]*right_product
            right_product = right_product*nums[i]
        return ans
        