class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        indexes_s = {}

        for i, c in enumerate(s):
            if c not in indexes_s:
                indexes_s[c] = []
            indexes_s[c].append(i)

        indexes_t = {}
        for i, c in enumerate(t):
            if c not in indexes_t:
                indexes_t[c] = []
            indexes_t[c].append(i)
        

        possible = set()
        for c in indexes_s:
            possible.add(tuple(indexes_s[c]))

        passed = set()
        for c in indexes_t:
            tup = tuple(indexes_t[c])
            if tup not in possible:
                return False
            
            possible.remove(tup)

        
        if len(possible) > 0:
            return False

        return True
