class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        
        res = [] 
        for e in d1:
            if e in d2:
                for _ in range(min(d1[e], d2[e])):
                    res.append(e)
                    
        return res
