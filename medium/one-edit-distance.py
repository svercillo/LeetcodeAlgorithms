class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)

        if m > n:
            temp = s
            s = t
            t = temp

        m = len(s)
        n = len(t)
        
        def num_edit_dists(sind, tind, num_edits)->bool:

            if num_edits > 1:
                return num_edits

            if sind == m:
                return n - tind + num_edits

            if tind == n:
                return m - sind + num_edits
 

            while sind < m and tind < n:

                if s[sind] == t[tind]:
                    sind += 1
                    tind += 1
                else:
                    return min(
                        num_edit_dists(sind +1, tind +1, num_edits +1),
                        num_edit_dists(sind, tind+1 , num_edits + 1)
                    )
            
            if sind == m and tind < n:
                return num_edits + n- tind

            elif sind < m and tind == n:
                return num_edits + m - sind
                

            return num_edits

        sind, tind = 0,0

        return num_edit_dists(sind, tind, 0) == 1
        