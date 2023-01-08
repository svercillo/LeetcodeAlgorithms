class Solution:
    def numSplits(self, s: str) -> int:
        totals = {}

        for c in s:
            if c not in totals:
                totals[c] = 0

            totals[c] += 1

        res = 0
        freq = {}        
        for i, c in enumerate(s):
            if c not in freq:
                freq[c] = 0

            freq[c] += 1

            nunique_totals = 0
            invalid = False
            for k in totals:
                if k not in freq:
                    nunique_totals += 1
                else:
                    if totals[k] - freq[k] > 0:
                        nunique_totals += 1

            if nunique_totals == len(freq):
                res += 1
            

        return res