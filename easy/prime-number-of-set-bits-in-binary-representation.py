class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        num = 0
        
        
        s = set({} )
        for i in range(L, R+1):
            string = str(bin(i))[2:]
            
            count = 0
            for c in string:
                if c =="1":
                    count += 1
                    
            if self.isPrime(count):
                # and count not in s:
                print(count)
                s.add(count)
                num += 1
                
        return num
                    
            
    def isPrime(self, n):
        if n ==1: return False
        for i in range (2, n):
            if n % i ==0:
                return False
                    
        return True
            
            
