class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # greedy sliding window 

        n = len(s)
        lp, rp = 0, 0
        curr = 0

        @cache
        def value(lp, rp): 
            # inclusive
            if lp == rp:
                return int(s[lp])

            return value(lp + 1, rp) + int(s[lp]) * 10 ** (rp -lp)

        num_partitions = 1
        while rp < n:
            
            
            if k < int(s[rp]): return -1

            if value(lp, rp) <= k:
                pass
            else:
                lp = rp
                num_partitions += 1
                
            rp += 1
            
        return num_partitions