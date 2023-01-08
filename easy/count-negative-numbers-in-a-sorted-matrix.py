class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(sum(1 for c in arr if c < 0) for arr in  grid)
