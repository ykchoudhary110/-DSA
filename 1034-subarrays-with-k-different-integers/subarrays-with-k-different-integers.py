class Solution:
    
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def atmost(k):
            if k<=0:
                return 0
            left = 0
            freq = {}
            res = 0
            for right in range(len(nums)):
                freq[nums[right]]= freq.get(nums[right],0 )+1

                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1
                res+=right - left+1 # Counts subarrays ending at right with at most k distinct integers; subtract atMost(k-1) to get exactly k.
            return res

        return atmost(k)-atmost(k-1)

    
            
                



        