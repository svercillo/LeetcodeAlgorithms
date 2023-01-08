class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)


        def dfs(size):
            starting = 0
            invalid = False 
            while starting < size:
                
                first = s[starting]
                i = starting
                while i < n:
                    
                    if s[i] != first:
                        invalid = True
                        break 
                    i += size
                starting +=1

                if invalid: break
            
            return not invalid


        for size in range(1, n //2 +1):
            if n % size == 0: 
                if dfs(size): return True

        return False
