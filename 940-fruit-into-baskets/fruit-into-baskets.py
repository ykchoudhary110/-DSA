class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        



        left = 0
        res = 0
        freq ={}

        for right in range(len(fruits)):
            freq[fruits[right]]= freq.get(fruits[right] ,0)+1

            while len(freq)>2:
                freq[fruits[left]]-= 1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1 #if not done then left wil be on zero always adn then right - left +1 will be wrong at any case

            res = max(res, right - left +1)#why rihgt - left +1 becuase in point 2 ruels stictly says it should be continous in different tone try to understand it
        return res

        