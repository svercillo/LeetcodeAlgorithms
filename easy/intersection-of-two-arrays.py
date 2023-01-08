class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set()
        for n in nums1:
            s1.add(n)
            
        s2 = set()
        for n in nums2:
            s2.add(n)
            
        return s1.intersection(s2)
            
