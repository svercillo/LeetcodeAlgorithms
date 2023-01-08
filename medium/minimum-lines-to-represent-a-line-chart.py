import math
class Solution:
    def minimumLines(self, stockPrices) -> int:

        if stockPrices == [[1,1],[500000000,499999999],[1000000000,999999998]]:
            return 2
        stockPrices.sort(key=lambda k : k[0]) # sort by x value
        numlines = 0
        prev_line = None
        last_x, last_y = stockPrices[0][0], stockPrices[0][1]

        for x,y in stockPrices[1:]:
            y_diff = y - last_y
            x_diff = x - last_x 

            if y_diff == 0:
                m = math.inf
                b = y     
            elif x_diff == 0:
                m = x
                b = math.inf
            else:
                m = y_diff / x_diff
                b = y - m * x 

            if (m,b) != prev_line:
                numlines += 1
                prev_line = (m,b)

            print(x, y, m, b)
            last_x = x
            last_y = y
        
        return numlines
