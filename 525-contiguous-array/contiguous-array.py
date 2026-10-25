class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
 


        res = 0
        current_sum = 0
        first_seen = {0:-1}#it says 0 exiested at imageinary index -1 which is not exisit reality helps to calcuate everything easily

        for i , num in enumerate(nums):
            # enumerate gives index and value of a num
            if num==0:
                current_sum-=1
            else:
                current_sum+=1

            if current_sum in first_seen:
                length= i-first_seen[current_sum]
                #this will minus current sum index form the currrent index
                res = max(res, length)
            else:
                first_seen[current_sum]=i#this iwll add the current sum with its index in the first seen 

        return res
# #         The easiest way to remember this code
# # - if current_sum in first_seen → I've seen this balance before, so calculate the subarray length.
# # - length = i - first_seen[current_sum] → Find how long that balanced subarray is.
# # - res = max(res, length) → Keep the longest length found so far.
# # - else: first_seen[current_sum] = i → It's a new balance, so remember its first position.
#       