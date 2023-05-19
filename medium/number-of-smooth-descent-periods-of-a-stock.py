class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        n = len(prices)
        i = 0
        total = 0
        while i < n:

            
            start = i
            end = i
            while i < n -1 and prices[i] - 1 == prices[i+1]:
                i += 1 
                end = i


            size = end - start + 1

            print(size)

            total += size * (size +1) // 2
            i += 1

        

        return total
