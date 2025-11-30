class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n1 + n2 != n3: 
            return False
        

        @cache
        def ispossible(p1, p2):
            if p1 == n1 and p2 == n2:
                return True

            req = s3[p1 + p2]

            if p1 < n1 and s1[p1] == req:
                if ispossible(p1+1,p2):
                    return True

            if p2 < n2 and s2[p2] == req:
                if ispossible(p1, p2 + 1):
                    return True
            return False

        return ispossible(0,0)
