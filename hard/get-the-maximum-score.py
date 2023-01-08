class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        nl, nr = len(nums1), len(nums2)
        map1, map2  = {}, {}
        for i,e in enumerate(nums1): 
            map1[e] = i
        for i,e in enumerate(nums2): 
            map2[e] = i

        
        portals = []
        portal_vals = {}
        for e in nums1:
            if e in map1 and e in map2:
                portals.append(e)
                portal_vals[e] =0


        lp, rp = 0, 0
        for p in portals: 
            lind, rind = map1[p], map2[p]
            lsum = 0
            rsum = 0
            while lp <= lind:
                lsum += nums1[lp]
                lp += 1

            while rp <= rind:
                rsum += nums2[rp]
                rp += 1

            portal_vals[p] = max(lsum, rsum)

        score = 0
        for p in portal_vals:
            score += portal_vals[p]

        
        
        lsum, rsum = 0, 0
        while lp < nl: 
            lsum += nums1[lp]
            lp += 1

        while rp < nr:
            rsum += nums2[rp]
            rp += 1

    
        score += max(lsum, rsum)

        return score % (10 ** 9 + 7)
