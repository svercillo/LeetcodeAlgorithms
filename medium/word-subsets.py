from collections import deque
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        q = deque()
        freq = {} 

        max_fruit = 0
        for f in fruits:
            if len(freq) < 2 or f in freq:
                q.append(f)
                if f not in freq:
                    freq[f] = 0
                freq[f] += 1
            elif len(freq) == 2 and f not in freq:
                while len(freq) == 2:
                    top = q.popleft()
                    freq[top] -= 1
                    if freq[top] == 0:
                        freq.pop(top)
                q.append(f)
                freq[f] = 1
            max_fruit = max(max_fruit, len(q))

        return max_fruit
