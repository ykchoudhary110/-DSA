class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        res = 0
        product = 1

        if k<=1:
            return 0

        for right in range(len(nums)):
            product *= nums[right]


            while product >= k:
                product //= nums[left]
                left+=1

            res+= right - left + 1 # it counts all the subarray form teh right msot pointer that it right will be there in the subarray adn other thant that is already counted when right was at its last positon 
            

        return res


#         For counting all valid subarrays:

# result += right - left + 1



        