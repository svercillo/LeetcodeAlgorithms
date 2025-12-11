class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:        
        p1, p2  = 0, 0

        houses.sort()
        heaters.sort()


        def findrad(houses, heaters,reverse):
            dist = [math.inf] * len(houses)
            p2 = 0
            radius = 0
            for i, hloc in enumerate(houses):

                while p2 < len(heaters) and hloc > heaters[p2]: 
                    p2 += 1
                
                if p2 == len(heaters):
                    break
                # print('house', hloc, "heat", heaters[p2], heaters[p2] - hloc)

                if not reverse:
                    dist[i] = heaters[p2] - hloc
                else: 
                    dist[len(houses) -1 - i] = heaters[p2] - hloc

            return dist

        fdist = findrad(houses, heaters, False)
        bdist = findrad(
            [-e for e in sorted(houses, reverse =True)],
            [-e for e in sorted(heaters, reverse=True)], 
            True
        )


        return max([min(e) for e in zip(fdist, bdist)])

        print(fdist, bdist)

            
            
            
