class Solution:
    def maxRemovals(self, source: str, pattern: str, target: List[int]) -> int:

        target.sort()


        pind = 0
        for i in range(target[0]):
            if pind < len(pattern) and source[i] == pattern[pind]:
                pind += 1

        @cache
        def maxRemovals(tind, pind):

            # print(tind, pind)
            if pind == len(pattern):
                return len(target) - tind

            if tind == len(target):
                if pind != len(pattern):
                    return -math.inf
                return 0


            startInd = target[tind]
            if tind + 1 == len(target): 
                endInd = len(source)
            else:
                endInd = target[tind+ 1]
            
            # try take index
            pindCpy = pind
            for i in range(startInd, endInd):
                if i == startInd:
                    continue # skip because we don't want to remove
                if pindCpy < len(pattern) and source[i] == pattern[pindCpy]:
                    pindCpy += 1
            res2 = maxRemovals(tind + 1, pindCpy) + 1

            # don't take index
            pindCpy = pind
            for i in range(startInd, endInd):
                if pindCpy < len(pattern) and source[i] == pattern[pindCpy]:
                    pindCpy += 1
            res1 = maxRemovals(tind + 1, pindCpy)


            # print(tind, pind, (res1, res2))
            return max(res1, res2)

            
        return maxRemovals(0, pind)
