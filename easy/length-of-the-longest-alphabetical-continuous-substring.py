class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        n = len(blocks)
        nB = 0
        for i in range(k):
            if blocks[i] == "B":
                nB += 1
        
        start = 0
        end = k
        
        mB = nB
        
        while end != n:
            if blocks[start] == "B":
                nB -= 1
            if blocks[end] == "B":
                nB += 1
        
            mB = max(mB, nB)
            start += 1
            end += 1
        
        return k - mB
            
        
