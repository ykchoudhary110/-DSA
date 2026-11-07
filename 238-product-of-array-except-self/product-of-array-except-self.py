class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        left_product = 1
        right_product = 1
        n = len(nums)
        for i in range(n):
            ans.append(left_product)
            left_product = nums[i]*left_product
        for i in range(n-1, -1, -1):
            ans[i] = ans[i]*right_product
            right_product = right_product*nums[i]
        return ans 

#         ans = []
#         left_product = 1
#         right_product = 1
#         n =len(nums)
#         for i in range(n):
#             ans.append(left_product)
#             left_product = left_product*nums[i]#left product will be multilplied by element comming in nusm[i] as product it equal to that For index 0: There are NO numbers before it. So the answer must be 1.
# # For index 1: Only nums[0] is before it.
# # For index 2: nums[0] * nums[1] are before it.
# # For index 3: nums[0] * nums[1] * nums[2] are before it.
#         for i in range(n-1, -1, -1): # it means start fom n-1 and end before element at -1 that is 0 and take -1 steps
#             ans[i]= ans[i]*right_product #thsi means mulitiple existing ans[i] which was appended whiel doign left_product
#             right_product = right_product*nums[i]
#         return ans
        