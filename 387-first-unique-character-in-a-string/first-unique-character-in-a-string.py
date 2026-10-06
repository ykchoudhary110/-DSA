class Solution:
    def firstUniqChar(self, s: str) -> int:
        left = 0
       
        freq= {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) +1

        while left<len(s):
            if freq[s[left]]==1:
                return left
            left+=1
        return -1

        