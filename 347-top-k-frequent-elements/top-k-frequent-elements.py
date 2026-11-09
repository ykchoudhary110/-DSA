class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num]= count.get(num,0)+1

        bucket = [[] for i in range(len(nums)+1)] # why we are creating len(nums)+1 because in len of nums is 5 then ti will left the end index while creatign so need to add one to it
        for num, freq in count.items():#count items calls both the key and value
            bucket[freq].append(num)

        res = []
        for freq in range(len(bucket)-1 , 0 ,-1):
            for num in bucket[freq]:
                res.append(num)
                if len(res)==k:
                    return res
        return res
            


        