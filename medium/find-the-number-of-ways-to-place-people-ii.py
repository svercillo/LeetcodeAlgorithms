class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda k : (k[0], -k[1]))

        n = len(points)
        print(points)
        


        total = 0
        # for each point find the matching point
        for i in range(n-1):
            minh = -math.inf
            x1,y1 = points[i]
            for j in range(i+1, n):
                x2,y2 = points[j]

                if y2 > y1 or y2 <= minh:
                    continue
                minh = y2

                total += 1

        return total

        
            


        
