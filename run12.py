from bisect import bisect_left
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) < len(nums2):
            t = nums2
            nums2 = nums1
            nums1 = t
        total = len(nums1) + len(nums2)

        n = len(nums1)

        def condition(l, r): 
            m1 = (l + r) // 2
            e1 = nums1[m1]

            m2 = bisect_left(nums2, e1)

            num_left_side = m1 + m2 + 2

            if num_left_side < num_left_side // 2:
                return -1
            elif num_left_side == 0:
                return 0
            else:
                return 1

            
            


        l, r = 0, n

        while condition(l, r):
            m = (l + r) // 2

            if 
            

        