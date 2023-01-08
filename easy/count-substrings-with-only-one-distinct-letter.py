class Solution:
    def countLetters(self, s: str) -> int:
        n = len(s)
        dp = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append("-")
            dp.append(row)

        res = n
        for i in range(n):

            if i < n - 1:
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = s[i]
                    res += 1

            dp[i][i] = s[i]

        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if (
                    dp[i + 1][j - 1] != "-"
                    and s[i] == s[j]
                    and s[i] == dp[i + 1][j - 1]
                ):
                    res += 1
                    dp[i][j] = dp[i + 1][j - 1]

        return res
