class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_s = str(low)
        
    
        res = []

        for s_len in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10):
                carr = []
                invalid = False
                for i in range(s_len):
                    d = start + i
                    if d > 9:
                        invalid = True
                        break
                    
                    carr.append(str(d))
            
                    
                    v = int("".join(carr))
                
                if invalid:
                    continue

                if low <= v <= high:
                    res.append(v)
                
                if v > high:
                    continue
            

        return res
