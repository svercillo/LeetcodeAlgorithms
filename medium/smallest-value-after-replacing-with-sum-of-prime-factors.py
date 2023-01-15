class Solution:
    def smallestValue(self, n: int) -> int:
        
        @cache
        def smallest(num):
            init_num = num
            total_sum = 0
            if num == 1:
                return 0
            elif num == 2:
                return 2
            
            for n in range(2, round(num ** 0.5) +2):
                if n >= num:
                    break 
                if num % n == 0:
                    total_sum = smallest(num // n) + smallest(n)
                    break
                
            if total_sum == 0: # number is prime
                return num 
            
            return total_sum



        last = None
        curr = smallest(n)
        while curr != last:
            last = curr
            curr = smallest(curr)

        
        return int(curr)
                
                
