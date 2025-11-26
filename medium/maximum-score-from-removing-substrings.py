class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        c1, c2 = 'a', 'b'
        t1, t2 = x, y
        if x < y:
            t1, t2 = y, x
            c1, c2 = 'b', 'a'

        x, y = t1, t2

        res = 0
        na, nb = 0, 0
        for i, c in enumerate(s):
            if c == c1:
                na += 1
            elif c == c2:
                if na:
                    res += x
                    na -= 1
                else:
                    nb += 1
            else:


                res += min(na, nb) * y
                na, nb = 0,0
        res += min(na, nb) * y

        return res


    
