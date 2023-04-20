class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        @cache
        def min_dist(ind1, ind2):
            m = len(word1)
            n = len(word2)

            if ind1 == m:
                return n - ind2

            if ind2 == n:
                return m - ind1

            mdist = math.inf
            if word1[ind1] == word2[ind2]:
                mdist = min_dist(ind1+1, ind2+1)


            mdist = min(
                min_dist(ind1+1, ind2) + 1,
                mdist
            )

            mdist = min(
                min_dist(ind1+1, ind2) + 1,
                mdist
            )

            mdist = min(
                min_dist(ind1, ind2+1) + 1,
                mdist
            )

            return mdist
            
        return min_dist(0, 0)
