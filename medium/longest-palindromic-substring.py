class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispal(s):
            n = len(s)
            for i in range(n // 2):
                if s[i] != s[n - 1 - i]:
                    return False
            return True

        msize = 0
        mstring = s[0]
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):

                if j + 1 - i > msize:
                    substring = s[i : j + 1]
                    if ispal(substring):
                        msize = j + 1 - i
                        mstring = substring

        return mstring


res = Solution().longestPalindrome("ac")

print(res)
