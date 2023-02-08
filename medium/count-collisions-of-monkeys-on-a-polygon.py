class Solution:
    def monkeyMove(self, n: int) -> int:
        
        def mod_exp(x,y, n):
            
            if y == 0:
                return 1
            
            z = mod_exp(x, y // 2, n)
            
            if y % 2 == 0:
                return z * z % n
            
            else:
                return x * z *z % n 
            
            
            
        N = 10 ** 9 + 7
        return (mod_exp(2, n, N) -2 + N) % N ;
