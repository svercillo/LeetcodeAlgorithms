class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(string):
            last = string[0]
            c = 0
            res = []
            for e in string:
                if e == last:
                    c += 1
                else:
                    res.append(str(c))
                    res.append(last)
                    c = 1
                
                last = e
            
            res.append(str(c))
            res.append(e)
            return "".join(res)
        
        value = "1"
        for _ in range(n-1): 
            value = rle(value)

        return value





