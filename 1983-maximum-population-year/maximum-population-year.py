class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        births = []
        deaths = []
        for birth, death in logs:
            births.append(birth)
            deaths.append(death)
        births.sort()
        deaths.sort()
        b = 0
        d= 0 #fro birth and death

        max_pop = 0
        current_pop  = 0
        max_year = births[0]
        while b<len(logs):
            if births[b]<deaths[d]:
                current_pop=current_pop+1
                if current_pop >max_pop:
                    max_pop= current_pop
                    max_year = births[b]
                b = b+1
            else:
                current_pop = current_pop-1
                d= d+1
        return max_year

        




        