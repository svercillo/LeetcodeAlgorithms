class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        freq1 = defaultdict(lambda : 0)

        for c in word1: 
            freq1[c] += 1
        
        for c in word2:
            freq1[c] -=1

        for c in freq1:
            if abs(freq1[c]) > 3:
                return False

        return True
