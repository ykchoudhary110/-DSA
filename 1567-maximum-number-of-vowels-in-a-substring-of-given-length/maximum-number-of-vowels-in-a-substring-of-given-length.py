class Solution:
    def maxVowels(self, s: str, k: int) -> int:


        vowels = 'aeiou'

        count = 0
        for i in range(k):
            if s[i] in vowels:
                count+=1

        res = count

        for right in range(k, len(s)):
            if s[right-k] in vowels:
                count-=1

            if s[right] in vowels:
                count+=1

            res = max(res, count)

        return res


        # vowels = 'aeiou'

        # count  =0
        # for i in range(k):
        #     if s[i] in vowels:
        #         count+=1
            
        # res = count

        # for right in range(k,len(s)):
        #     if s[right-k] in vowels:
        #         count -=1

        #     if s[right] in vowels:
        #         count+=1

        #     res = max(res, count)

        # return res

        