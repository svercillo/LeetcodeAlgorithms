    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def min_cost(ind):
            n = len(days)
            if ind >= n:
                return 0

            # 1 day pass
            res1 = min_cost(ind +1) + costs[0]
            
            # 7 day pass 
            j = ind + 1
            while j < n and days[j] - days[ind] < 7:
                j += 1
            res7 = min_cost(j) + costs[1]

            # 30 day pass

            j = ind + 1
            while j < n and days[j] - days[ind] < 30:
                j += 1
            res30 = min_cost(j) + costs[2]

            return min(res1, res7, res30)

        return min_cost(0)
