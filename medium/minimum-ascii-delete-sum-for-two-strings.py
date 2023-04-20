class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        
        @cache
        def min_sum(ind1, ind2):
            
            m, n = len(s1), len(s2)

            if ind1 == m:
                rem_sum = 0
                for i in range(ind2, n):
                    rem_sum += ord(s2[i])
                return rem_sum

            elif ind2 == n:
                rem_sum = 0
                for i in range(ind1, m):
                    rem_sum += ord(s1[i])
                return rem_sum

            
            msum = math.inf
            if s1[ind1] == s2[ind2]:
                msum = min_sum(ind1+1, ind2+1)

            msum = min(
                min_sum(ind1 + 1, ind2) + ord(s1[ind1]),
                msum
            )

            msum = min(
                min_sum(ind1, ind2 + 1) + ord(s2[ind2]),
                msum
            )

            return msum


        return min_sum(0, 0)
