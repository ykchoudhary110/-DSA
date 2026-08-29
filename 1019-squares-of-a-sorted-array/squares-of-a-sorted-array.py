from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size= len(nums)
        neg = []
        pos = []
         #for sepration tow array

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        #for no negative no.

        if len(neg) == 0:
            return [x*x for x in pos]
        
#for if no . postive no. is there

        if len(pos) == 0:
            neg = [x*x for x in neg]
            neg.reverse()
            return neg
        # if both negative and positive no. exits

        neg = [x*x for x in neg][::-1]
        pos = [x*x for x in pos]

        n, m= len(neg),len(pos)
        
        res = []
        i = j = 0

        while i<n and j<m:
            if neg[i]<pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1
        while i<n:
            res.append(neg[i])
            i+=1
        while j<m:
            res.append(pos[j])
            j+=1
        
        return res

        

        


        