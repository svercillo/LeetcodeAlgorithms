class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        seen = set()
        freqs = []
        for word in stickers:
            freq = [0 for _ in range(26)]
            for c in word:
                freq[ord(c) - ord("a")] += 1
                seen.add(c)

            freqs.append(freq)

        remainingFreq = [0 for _ in range(26)]
        for c in target:
            if c not in seen: 
                return -1            
            remainingFreq[ord(c) - ord("a")] += 1

        
        def printRem(freq):
            res = defaultdict(lambda : 0 )
            for i in range(26):
                if freq[i] != 0:
                    res[chr(i+ ord("a"))]  = freq[i]

            print(res)

        @cache
        def minMoves(remainingFreq):
            if max(remainingFreq) == 0:
                return 0 # finished

            mMoves = math.inf            
            for freq in freqs:
                remainingCpy = [v for v in remainingFreq]

                for c, v in enumerate(freq): 
                    remainingCpy[c] = max(0, remainingCpy[c] - v)

                remainingCpyTup = tuple(remainingCpy)

                if remainingCpyTup != remainingFreq:
                    res = minMoves(remainingCpyTup) + 1
                    if res < mMoves:
                        mMoves = res

            return mMoves
                

        
        return minMoves(tuple(remainingFreq))

        
