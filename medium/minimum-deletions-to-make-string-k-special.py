class Solution:

    def _createfreq(self, word):
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1

        return sorted(list(freq.values()))

    def _find_smallest_freq(self, freq):
        return min(freq.values())

    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = self._createfreq(word)

        num_to_remove = 0
        res = math.inf
        for i, v in enumerate(freqs):            
            f1 = freqs[i]
            to_remove = 0
            for j in range(i+1, len(freqs)):
                f2 = freqs[j]
                
                if f2 - f1 > k:
                    to_remove += f2 - (f1 + k) 
            


            localrems = to_remove + num_to_remove
            res = min(res, localrems)

            
            num_to_remove += v

        return res
        
