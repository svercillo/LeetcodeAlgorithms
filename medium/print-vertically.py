class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()

        mlen = max([len(w) for w in words])
        res = [list() for _ in range(mlen)]
        ps = [0] * len(words)



        for ind in range(mlen): 
            for wind in range(len(words)):
                if ps[wind] == len(words[wind]): 
                    res[ind].append(" ")
                else:
                    res[ind].append(words[wind][ps[wind]])
                    ps[wind] += 1 

            
                
        return ["".join(e).rstrip() for e in res]

        
        
            
