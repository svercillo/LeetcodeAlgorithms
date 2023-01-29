from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        sstack = deque()
        tstack = deque()

        for c in s:
            if c == "#":
                if len(sstack):
                    sstack.pop()
            else:
                sstack.append(c)

        for c in t:
            if c == "#":
                if len(tstack):
                    tstack.pop()

            else:
                tstack.append(c)

        return sstack == tstack   
