class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:        
        count = 0

        largest_len = math.ceil((1 + (1 + 8 * n) ** 0.5) / 2) 
        for l in range(1, largest_len + 1):


            start_offset = (2 * n - l** 2) / (2 * l) + 0.5 

            if start_offset.is_integer() and start_offset > 0: 
                count += 1

        return count
