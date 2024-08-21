class Solution:


    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        self.A = A
        self.B = B
        return max(
            self.maxBoost(0, True),
            self.maxBoost(0, False)
        )


    @cache 
    def maxBoost(self, i, isTop): 
        A = self.A
        B = self.B
        size = len(A)

        if i >= size:
            return 0

        return max(
            self.maxBoost(i + 1, isTop) + (A[i] if isTop else B[i]),
            self.maxBoost(i +2, not isTop) + (A[i] if isTop else B[i])
        )
