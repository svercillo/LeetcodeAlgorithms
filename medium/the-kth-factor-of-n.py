class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        res = set()
        res.add(1)

        for i in range(2, int(n** 0.5) + 1):
            if n % i == 0:
                res.add(i)
                res.add(n // i)


        print(res)
        res.add(n)

        res = sorted([r for r in res])
        
        return res[k-1] if k -1 < len(res) else -1
        
