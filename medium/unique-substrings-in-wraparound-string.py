class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        i = 0
        n = len(s)

        total = 0
        
        highest_prev = defaultdict(int)

        count = 1
        last = None 
        for c in s:

            if last is None or not(
                ord(c) == ord(last) + 1
                or ord(c) == 97 and ord(last) == 122
            ):
                last = c
                count = 1
            else:            
                count += 1
                
            highest_prev[c] = max(highest_prev[c], count)
            last = c

        total = 0

        for c in highest_prev: 
            
            l = highest_prev[c]

            total += l


        return total
