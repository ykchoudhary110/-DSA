class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        p_freq = {}
        window_freq = {}

        for ch in p:
            p_freq[ch] = p_freq.get(ch, 0)+1

        left = 0
        result = []

        for right in range(len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) +1

            if right - left + 1 > len(p):
                window_freq[s[left]] -= 1

                if window_freq[s[left]]==0:
                    del window_freq[s[left]]

                left+=1

            if right - left +1 == len(p):
                if window_freq == p_freq:
                    result.append(left)
                    

        return result

        