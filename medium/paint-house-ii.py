import math
from pprint import pprint


class Solution:
    def minCostII(self, costs) -> int:
        for cost in costs:
            print(cost)
        n = len(costs)
        m = len(costs[0])

        if n == 1:
            return min(costs[0])

        dp = []
        for i in range(n):
            row = []
            for j in range(m):
                if i == 0:
                    row.append(costs[i][j])
                else:
                    row.append(math.inf)
            dp.append(row)

        for i in range(1, n):  # ith house
            print(dp)
            for j in range(m):  # three colours
                inds = set([i for i in range(m)])
                inds.remove(j)

                min_cost = math.inf
                for ind in inds:
                    if dp[i - 1][ind] < min_cost:
                        min_cost = dp[i - 1][ind]

                dp[i][j] = costs[i][j] + min_cost

        return min(dp[-1])


res = Solution().minCostII([[1, 3], [2, 4]])

print(res)
