class Solution:
    def sumZero(self, n: int) -> List[int]:
        cs = 0

        res = []
        if n % 2 == 0:
            for i in range(n):
                i = i + 1
                if i % 2 == 0:
                    res.append(i // 2)
                else:
                    res.append(-i // 2 )

        else:
            for i in range(n-1):
                i = i + 1
                if i % 2 == 0:
                    res.append(i // 2)
                else:
                    res.append(-i // 2)
            res.append(0)
    
        return res            
            
