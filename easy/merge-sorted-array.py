class Solution:
    def merge(self, n1, m: int, n2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        endind = m + n - 1
        l = m - 1
        r = n - 1

        while l >= 0:
            while r >= 0 and n1[l] < n2[r]:
                n1[endind] = n2[r]
                endind -= 1
                r -= 1

            n1[endind] = n1[l]
            endind -= 1
            l -= 1

        while r >= 0:
            n1[endind] = n2[r]
            endind -= 1
            r -= 1

        print(n1)
