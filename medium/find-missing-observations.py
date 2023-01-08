class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        total_value = (m + n) * mean
        current_value = sum(rolls)
        diff_value = total_value - current_value

        
        if not (1* n <= diff_value <= 6 * n):
            return [] # impossible

        

        mean_added = diff_value // n
        extra = diff_value % n

        print(mean_added, extra)

        res = []

        for i in range(n):
            res.append(mean_added)

        print(res)
        for i in range(n):
            print(extra)
            if extra > 0:
                extra_added = min(6 - res[i], extra)
                res[i] += extra_added 
                extra -= extra_added
            else: 
                break

        return res        
