class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        for i, a in enumerate(arr):
            if i == a:
                return i
            
        return -1
