class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        i, n = 0, len(s)

        count = 0
        start = 0
        chars = set()
        while i < n:
            c = s[i]

            if c in chars:
                while start < i and s[start] != c:
                    chars.remove(s[start])
                    start += 1

                start += 1
                i += 1
                continue

                # return count

            chars.add(c)
            if i - start == k - 1:
                chars.remove(s[start])
                count += 1
                start += 1

            i += 1

        return count
