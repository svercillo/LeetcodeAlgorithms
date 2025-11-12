class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        

        indexes = defaultdict(list)
        for i,e in enumerate(nums2):
            indexes[e].append(i)

        def findnxtelement(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = (l+ r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l

            # for i, e in enumerate(nums):
            #     if e > target:
            #         return i

            # return len(nums)

        
        @cache
        def process(ind1, used2):
            if ind1 == len(nums1):
                return 0
            value = nums1[ind1]

            inds = indexes[value] 
            spot = findnxtelement(inds, used2)


            mvalue = process(ind1 + 1, used2)
            
            for useind in range(spot, len(inds)):
                res = process(ind1+ 1, inds[useind]) + 1
                mvalue = max(res, mvalue)
            return mvalue
        

        return process(0, -1)
            

            

            

