class Solution:
    def countElements(self, arr: List[int]) -> int:
        freq = {}

        for n in arr:
            if n not in freq:
                freq[n] = 0

            freq[n] += 1

        c = 0
        for n in freq:
            if n + 1 in freq:
                c += freq[n]

        return c
