class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        low = 0 # low will tell where to keep the zero
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[low] , nums[i] = nums[i],nums[low]
                low+=1
                # i+=1
            # else:
                # i+=1
        """
        Do not return anything, modify nums in-place instead.
        """

        # low = 0

        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[low] , nums[i] = nums[i], nums[low]
        #         low +=1
        #         i +=1
        #     else:
        #         i+=1
   