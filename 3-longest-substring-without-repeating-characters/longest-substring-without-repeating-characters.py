class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        res = 0


        for right in range(len(s)): 
            # it means first the choose betwwen 0 and right and then we get a in here we will simply return freq using +1 to it otherwise intially its zero
#             Who came? → s[right]

# How many times have they come before? → freq.get(..., 0)

# They came one more time → +1

# Update their record → freq[...]

            freq[s[right]]=freq.get(s[right], 0)+1# add right chararcter to freq




            while freq[s[right]]>1:
                #when window is wrong
                freq[s[left]] -= 1
              

                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1

            res = max(res,right -left +1) # in place of len(freq ) you can use right - left +1

        return res

        
        