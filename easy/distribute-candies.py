class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = set([c for c in candyType])

        return min(len(d), len(candyType) // 2)
        
