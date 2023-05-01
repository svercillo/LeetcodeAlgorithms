class Solution:
    def minSteps(self, s: str, t: str) -> int:

        freqs = defaultdict(lambda: 0)
        freqt = defaultdict(lambda: 0)

        for c in s:
            freqs[c] += 1

        for c in t:
            freqt[c] += 1


        print(freqs, freqt)
        total = 0
        for c in freqs:
            if freqs[c] > freqt[c]:
                total += freqs[c] - freqt[c]

        
            

        return total

        

