class Solution:
    def shortestToChar(self, s: str, target: str) -> List[int]:

        n = len(s)
        dp = [-1] * n
        q = []
        for i, c in enumerate(s):
            if c == target:
                q.append(i)
        
        
        dist = 0
        while len(q):
            new_q = []
            for index in q:
                if dp[index] != -1:
                    continue # dp already set
                dp[index] = dist


                if index + 1 < n:
                    new_q.append(index + 1)

                if index - 1 >= 0: 
                    new_q.append(index - 1)
            dist += 1
            q = new_q

        return dp
