class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        
        counting_char = s[0]
        
    
        def count(counting_char):
            nonlocal s

            total = 0 
            count = 0x
            oppcount = 0
            for i in range(n):
                if s[i] == counting_char:
                    if oppcount:
                        total += min(count, oppcount)
                        oppcount = 0
                        count = 0
                    
                    count += 1
                else:
                    oppcount += 1
                    
            if s[-1] != oppcount:
                total += min(count, oppcount)
                
            return total
                    
            
                    
                    
        return count("0") + count("1")
