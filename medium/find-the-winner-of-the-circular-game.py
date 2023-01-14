class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        skip = set()

        curr = n -1
        first = True
        while len(skip) < n -1:
            temp_k = k
            
            while True:

                if not first and curr not in skip:
                    temp_k -= 1

                first = False

                if not temp_k:
                    skip.add(curr)
                    break

                curr += 1
                curr %= n 




        for i in range(n):
            if i not in skip:
                return i + 1
