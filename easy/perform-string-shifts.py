from collections import deque


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        totalshift = 0
        for d, a in shift:

            if d == 0:
                a = -a
            totalshift += a

        q = deque()
        for c in s:
            q.append(c)

        reverse = totalshift < 0
        totalshift = abs(totalshift)

        while totalshift > 0:

            if not reverse:
                top = q.pop()
                q.appendleft(top)
            else:
                top = q.popleft()
                q.append(top)

            totalshift -= 1

        res = ""
        for c in q:
            res += c

        return res
