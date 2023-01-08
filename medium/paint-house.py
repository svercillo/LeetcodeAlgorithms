import math
from pprint import pprint


class Solution:
    def minCost(self, costs) -> int:
        for cost in costs:
            print(cost)
        n = len(costs)
        if n == 1:
            return min(costs[0])

        dp = []
        for i in range(n):
            row = []
            for j in range(3):
                if i == 0:
                    row.append(costs[i][j])
                else:
                    row.append(math.inf)
            dp.append(row)

        for i in range(1, n):  # ith house
            print(dp)
            for j in range(3):  # three colours
                inds = set([0, 1, 2])
                inds.remove(j)

                min_cost = math.inf
                for ind in inds:
                    if dp[i - 1][ind] < min_cost:
                        min_cost = dp[i - 1][ind]

                dp[i][j] = costs[i][j] + min_cost

        return min(dp[-1])
