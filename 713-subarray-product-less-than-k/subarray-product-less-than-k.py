class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        res = 0
        product =1
        if k<=1:
            return 0 # check example 2

        for right in range(len(nums)):
            product *= nums[right]

            #for window is worng
            while product>=k:
                product//= nums[left] # floor division 100/10 = 10.0 and in this 100//10= 10 
                left+=1
            
            res += right - left +1 # it includes all the subarray in the window and if you thing somehign is left no its not it has been already counted earlier with prvious itration so dont woory jsut go to chatgpt and it will exaplain it in a minute 

        return res


















#         left = 0
#         res = 0
#         product = 1

#         if k<=1:
#             return 0

#         for right in range(len(nums)):
#             product *= nums[right]


#             while product >= k:
#                 product //= nums[left]
#                 left+=1

#             res+= right - left + 1 # it counts all the subarray form teh right msot pointer that it right will be there in the subarray adn other thant that is already counted when right was at its last positon 
            

#         return res


# #         For counting all valid subarrays:

# # result += right - left + 1



        