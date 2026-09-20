class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        res = 0


        for right in range(len(s)): 
            freq[s[right]]=freq.get(s[right], 0)+1# add right chararcter to freq



            while freq[s[right]]>1:
                #when window is wrong
                freq[s[left]] -= 1
              

                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1

            res = max(res, right - left +1)

        return res

        
        