from functools import cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        @cache
        def num_visits(ind):
            nonlocal d

            total_visits = 0 
            for j in range(ind-1, ind - d -1, -1):
                if j < 0 or arr[j] >= arr[ind]:
                    break
                total_visits = max(total_visits, num_visits(j) + 1)

            for j in range(ind+1, ind+ d +1):
                
                if j >= n or arr[j] >= arr[ind]:
                    break
                total_visits = max(total_visits, num_visits(j) + 1)

            return total_visits

        n = len(arr)
        total_num_visits = 0
        for i in range(n):
            total_num_visits = max(total_num_visits, num_visits(i) + 1)
        return total_num_visits