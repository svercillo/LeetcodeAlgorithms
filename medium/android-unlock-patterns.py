class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # classic backtracking



        # given a valid pattern, how many valid patterns from there ?
        
        

        def numValidPatterns(pattern):
            nonlocal m, n
            used = set(pattern)

            # print(pattern)
            if len(pattern) >= m:
                total_valid = 1
            else:
                total_valid = 0

            for num in range(1, 10):
                
                if num in used:
                    continue

                if len(pattern) >= 1: 
                    if ( # horizontal line
                        (num -1) // 3 == (pattern[-1] -1) // 3 
                        and (
                            num % 3 == 1 and pattern[-1] % 3 == 0
                            or num % 3 == 0 and pattern[-1] % 3 == 1
                        )
                        and min(num, pattern[-1]) + 1 not in used
                    ):
                        continue

                    if abs(num - pattern[-1]) == 6 and min(num, pattern[-1]) + 3 not in used:
                        continue # vertical line

                    if sorted([num, pattern[-1]]) == [1, 9] and 5 not in used:
                        continue # top left- bottom right diag

                    if sorted([num, pattern[-1]]) == [3, 7] and 5 not in used:
                        continue # bottom left - top right diag
                    
                nxt_pattern = pattern.copy()
                nxt_pattern.append(num)

                if len(nxt_pattern) > n:
                    continue

                total_valid += numValidPatterns(nxt_pattern)

            return total_valid
            
        return numValidPatterns([])
                


