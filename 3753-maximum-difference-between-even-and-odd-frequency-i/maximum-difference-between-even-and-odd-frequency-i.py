class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch]= freq.get(ch,0)+1

        max_odd = 0
        min_even = float("inf")
        
        for count in freq.values():
            if count%2==0:
                min_even = min(count, min_even)
            else:
                max_odd = max(count, max_odd)
        return max_odd-min_even
                
        