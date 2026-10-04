class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k%n
        def reverse(left , right):
            while left<right:
                nums[left] , nums[right] = nums[right], nums[left]
                left+=1
                right -=1

        reverse(0 , n-1)
        reverse(0, k-1)
        reverse(k, n-1)


#         Original
# [1,2,3,4 | 5,6,7]

#        ↓ reverse everything reverse(0 , n-1)

# [7,6,5 | 4,3,2,1]

#        ↓ reverse first 3 reverse(0 , k-1)


# [5,6,7 | 4,3,2,1]

#        ↓ reverse rest (k , n-1)

# [5,6,7 | 1,2,3,4]
        
        """
        Do not return anything, modify nums in-place instead.
        """
        