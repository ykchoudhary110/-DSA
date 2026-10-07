class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            arr.append((nums[i],i))
            # it stores the nums values iwth indexes in new arr list

        # arr = [(nums[i], i) for i in range(len(nums))] the above three line can be written in this way too
        arr.sort()

    # Sort arr based on the number
        # [(3,0), (2,1), (4,2)]
        # becomes:
        # [(2,1), (3,0), (4,2)]

        left = 0
        right = len(arr)-1
        while left<right:
            # arr[left][0] means the VALUE at left
            # arr[right][0] means the VALUE at right
            #
            # Example:
            # arr[left]  = (2,1)
            # arr[right] = (4,2)
            #
            # arr[left][0]  = 2
            # arr[right][0] = 4
            #
            # So current = 2 + 4 = 6
            current = arr[left][0]+arr[right][0]

            if current==target:
                return [arr[left][1],arr[right][1]]
            elif current>target:
                right-=1
            else:
                left+=1

        
        