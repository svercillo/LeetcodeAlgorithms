class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a, b = set(), set()
        n = len(A)

        common = set()

        res = []

        for i in range(n):
            a.add(A[i])
            b.add(B[i])

            if A[i] in b and A[i] not in common:
                common.add(A[i])

            if B[i] in a and B[i] not in common:
                common.add(B[i])

            res.append(len(common))
            


        return res
