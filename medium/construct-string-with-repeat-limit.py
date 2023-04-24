from collections import deque

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = defaultdict(lambda : 0)
        
        for c in s:
            freq[c] += 1
        
        all_chars = [c for c in freq]

        all_chars.sort()
        stack = deque(all_chars)

        print(stack)
        res = []
        last_char_count = 0
        last_char = '%'

        unavail = None

        while len(stack):
            top = stack.pop()
            print(top, last_char, last_char_count)

            if not freq[top]:
                continue

            if top != last_char:
                last_char = top
                last_char_count = 0
                
            if last_char_count == repeatLimit:
                unavail = top
            else:
                last_char_count += 1
                freq[top] -=1 
                if freq[top] != 0:
                    stack.append(top)
                
                res.append(top)

            if unavail and top != unavail: 
                stack.append(unavail) # on char change, can always pop unavail

        return "".join(res)
