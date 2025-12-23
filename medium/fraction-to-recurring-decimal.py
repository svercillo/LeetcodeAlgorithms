class Solution:
    def fractionToDecimal(self, num: int, dem: int) -> str:
        isneg = (num < 0) ^ (dem < 0)

        if num == 0:
            return "0"
        num = abs(num)
        dem = abs(dem)


        def makestring(carr):
            return "".join([str(e) for e in carr])


        if num >= dem:
            timesfits = num // dem
            prefix = str(timesfits)
            num -= timesfits * dem
        else:
            prefix = "0"

        if not num: 
            return ("-" if isneg else "") + prefix

        prefix += "."
        carr = []
        visited = {}
        while num > 0:
            if num in visited:
                np = visited[num]

                return ("-" if isneg else "") + prefix + makestring(carr[:np]) + "(" + makestring(carr[np:]) + ")"
            
            visited[num] = len(carr)
            if num > dem:
                timesfits = num // dem
                for i, c in enumerate(str(timesfits)[::-1]):
                    carr[len(carr) -1 -i] += int(c)

                num -= timesfits * dem
            else:
                carr.append(0)
                num *= 10

            
        suff = makestring(carr)
        
        return ("-" if isneg else "") + prefix + suff
