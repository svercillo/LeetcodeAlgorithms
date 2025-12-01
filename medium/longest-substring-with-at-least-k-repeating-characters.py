
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # state:
        inds = {} # indexes of the at most k recent instaces of each c 
        res = 0


        for i, c in enumerate(s):
            if c not in inds:
                inds[c] = deque() # index q
            iarr = inds[c]
            iarr.append(i)

            if len(iarr) > k:
                iarr.popleft()

            start = 0 
            for c in inds:
                iarr = inds[c]
                if len(iarr) < k:
                    start = max(start, iarr[-1]+1)

            #print("start", start)
            for c in inds: 
                iarr = inds[c]
                if len(iarr) == k and iarr[0] < start <= iarr[-1]:
                    start = max(start, iarr[-1] + 1)



            #print("\tstart ", start)

            valid = False
            for c in inds:
                iarr = inds[c]
                if len(iarr) == k and start <= iarr[0]:
                    valid = True

            #print("\tvalid", valid, i - start + 1)
            if valid:
                res = max(res, i - start + 1)

        return res








