class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        best = [-1] * n

        largest = [0,0]
        for i in range(n):
            best[i] = largest
            if not largest:
                largest = (values[i], i)
            else:
                if values[i] > largest[0] - (i - largest[1]):
                    largest = (values[i], i)

        print(best)
        res = -math.inf
        for i, value in enumerate(values):
            if i != best[i][1]:
                res = max(res, value + best[i][0] - (i - best[i][1]))
            elif i > 0:
                res = max(res, value + best[i][-1] - (i - best[i-1][1]))

        return res

            
