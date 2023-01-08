from functools import lru_cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        @lru_cache
        def dfs(i, current):
            nonlocal n
            print(i, current)
            if i == n:
                return 1

            

            total = 0            
            match current:
                case "-":
                    total += dfs(1, "a")
                    total += dfs(1, "e")
                    total += dfs(1, "i")
                    total += dfs(1, "o")
                    total += dfs(1, "u")
                case 'a':
                    total += dfs(i+1, "e")
                case 'e': 
                    total += dfs(i+1, "a")
                    total += dfs(i+1, "i")
                case 'i': 
                    total += dfs(i+1, "a")
                    total += dfs(i+1, "e")
                    total += dfs(i+1, "o")
                    total += dfs(i+1, "u")
                case 'o':
                    total += dfs(i+1, "i")
                    total += dfs(i+1, "u")
                case 'u':
                    total += dfs(i+1, "a")

            return total


        return dfs(0, "-") % (10 ** 9 + 7)
