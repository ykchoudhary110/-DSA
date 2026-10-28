class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        res = 0
        current_sum = 0
        for num in nums:
            current_sum+=num
            needed = current_sum - k
            res+=freq.get(needed, 0)
            freq[current_sum]= freq.get(current_sum , 0)+1
        return res
   

     





        # # freq = {0:1}
        



        # # res = 0
        # # current_sum= 0
        # # for num in nums:
        # #     current_sum+=num #increse the current sum 

        # #     needed = current_sum - k #  # Find the earlier sum needed to make the subarray sum equal k fro exp we have curretn = 6 and k = 2 so we need 4 as summ adn its freq so that we can increse the res

        # #     res += freq.get(needed,0) # nwo in this res will increse if needed as key adn it value exists otherwise 0 

        # #     freq[current_sum] = freq.get(current_sum,0)+1 # nwo we are adding the curretn new sum value int the dict 

        # # return res









        
        