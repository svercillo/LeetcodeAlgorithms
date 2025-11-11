class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        l, r = 0, n-1


        def buildstring(ind, forw):
            incr = 1 if forw else -1

            res = []
            while 0<= ind < n and s[ind].isalpha():
                res.append(s[ind])
                ind += incr

            return "".join(res), ind

        def buildint(ind): 
            res = []
            while ind < n and s[ind].isdigit():
                res.append(s[ind])
                ind += 1
            return int("".join(res)), ind
        
        bmap = {}

        stack = deque()
        for i, c in enumerate(s):
            if c == "[":
                stack.append(i)
            elif c == "]":
                start = stack.pop()
                bmap[start] = i


        def solve(l, r):            
            prefix, l = buildstring(l, True)
            if l < n and s[l] == "]":
                return prefix

            if len(prefix) == r - l + 1 or l> r :
                return prefix # I'm just a string!!!

            mult, l = buildint(l)

            bend = bmap[l]
            l += 1 # skip bracket
            bvalue = solve(l, bend -1) # value of this bracket
            res = prefix + mult * bvalue +  solve(bend + 1, r)
            return res


        return solve(0, n-1)
