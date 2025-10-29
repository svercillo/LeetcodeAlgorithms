class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        for c in word:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        dials = sorted([freq[k] for k in freq], reverse=True)


        res = 0
        for (i, count) in enumerate(dials): 
            pushes = i // 8 + 1
            res += pushes * count


        return res
