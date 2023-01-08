class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        lp, rp = 0, 0

        while lp < n and rp < m:
            if s[lp] == t[rp]:
                lp += 1
                rp += 1

            else:
                lp += 1

        
        return m - rp

