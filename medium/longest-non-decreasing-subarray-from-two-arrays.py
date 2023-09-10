class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:

        # knapsack problem
        @cache
        def maxLength(i, left=True):
            if i == len(nums1) - 1:
                return 1
            
            # continue previous subarray
            prev = nums1[i] if left else nums2[i]
            possible = [1]
            if nums1[i+1] >= prev and nums2[i+1] >= prev:
                possible.append(maxLength(i+1, True) + 1)
                possible.append(maxLength(i+1, False) + 1)
            elif nums1[i+1] >= prev:
                possible.append(maxLength(i+1, True) + 1)
            elif nums2[i+1] >= prev:
                possible.append(maxLength(i+1, False) + 1)

            return max(possible)

        n = len(nums1)
        possible = []
        for i in range(n):

            possible.append(maxLength(i, True))
            possible.append(maxLength(i, False))

        return max(possible)
