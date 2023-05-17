class Solution:
    def lastRemaining(self, n: int) -> int:
        
        first_val = 1

        odd = True
        order =  1
        while n > 1:
            
            print(n, first_val, order, odd)
            if n % 2 == 1 or odd:
                first_val += order

            
            odd = not odd
            n //= 2
            order *= 2

        
        return first_val

