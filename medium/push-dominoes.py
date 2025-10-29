class Solution:
    def pushDominoes(self, arr: str) -> str:
        fallen = set()
        arr = [ c for c in arr]
        n = len(arr)


        q = {}
        for i,e in enumerate(arr):
            if e == "R":
                q[i] = 1
                arr[i] = "."
            elif e == "L":
                q[i] = -1
                arr[i] = "."


        while len(q):
            nq  = {} 

            for i in q:
                if arr[i] != ".":
                    continue
                d = q[i]
                arr[i] = "R" if d == 1 else "L"

                # try to propagate
                ni = i + d
                if not (0 <= ni < n):
                    continue

                if ni in nq:
                    nq.pop(ni)
                else:
                    nq[ni] = d
                
            q = nq

        return "".join(arr)                




