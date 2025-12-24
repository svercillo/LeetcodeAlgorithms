class Solution:
    def divide(self, dend: int, dsor: int) -> int:

        isneg = (dend < 0) ^ (dsor <0)
        dend, dsor = abs(dend) , abs(dsor)

        


        totaltimes = 0
        base = 0 
        while base + dsor < dend:
            ntimes = 1 
            multiple = dsor
            
            while base + multiple < dend:
                base += multiple
                totaltimes += ntimes

                multiple += multiple 
                ntimes += ntimes


        if dend - base == dsor:
            totaltimes += 1
        
        res = totaltimes * (-1 if isneg else 1)
        res = min(res, 2**31 -1)
        res = max(res, -2**31)

        return res


            


        
