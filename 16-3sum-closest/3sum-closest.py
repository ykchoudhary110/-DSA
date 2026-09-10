class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        mindif = float("inf")
        close = 0

        for i in range(n-2):
            left = i+1
            right = n-1

            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)


                if diff < mindif:
                    mindif = diff
                    close = sum

                if sum == target:
                    return sum

                if sum<target:
                    left+=1

                else:
                    right-=1

        return close


            

       



        