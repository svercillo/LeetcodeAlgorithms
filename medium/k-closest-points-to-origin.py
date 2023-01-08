class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return [tup[1] for tup in sorted([ ((p[0] ** 2 + p[1] **2) ** 0.5, p) for p in points], key=lambda tup: tup[0])[:k]]

    
        
