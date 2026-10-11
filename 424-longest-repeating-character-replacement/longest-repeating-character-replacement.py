class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        res = 0
        freq= {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0)+1
            max_freq= max(max_freq, freq[s[right]])

            while (right - left +1 ) - max_freq >k:#chekc wheater non matching charcter counter is greater than k and window shoudl be shifted 
                freq[s[left]]-=1
                left+=1
            res = max(res, right - left +1)
        return res
   






#         left = 0
#         freq = {}
#         res  = 0
#         max_freq =0

#         for right in range(len(s)):
#             freq[s[right]] = freq.get(s[right], 0)+1
#             max_freq = max(max_freq , freq[s[right]])

# #char that we can replace right - left +1 is length of window
#             while (right - left +1) -  max_freq > k:
#                 freq[s[left]]-=1
#                 left+= 1

#             res = max(res, right - left +1)

#         return res