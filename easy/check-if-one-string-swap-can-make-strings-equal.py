class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)

        if n1 != n2:
            return False

        a = []
        b = []
        for i in range(n1):
            if s1[i] != s2[i]:
                a.append(s1[i])
                b.append(s2[i])


        if len(a) == 0:
            return True
        elif not (len(a) == len(b) == 2):
            return False
        

        return a[::-1] == b
