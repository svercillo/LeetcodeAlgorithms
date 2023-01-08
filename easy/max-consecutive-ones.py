class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = nums
        n = len(s)

        m1 = 0
        m0 = 0

        t = True if s[0] == 1 else False  # 1 , 0 -> True
        start = 0
        end = 0

        while end < n:
            if t and s[end] == 1:
                end += 1

            elif not t and s[end] == 0:
                end += 1

            else:
                dist = end - start
                if t:
                    if dist > m1:
                        m1 = dist
                else:
                    if dist > m0:
                        m0 = dist

                start = end
                t = not t
        dist = end - start
        if t:
            if dist > m1:
                m1 = dist
        else:
            if dist > m0:
                m0 = dist

        return m1
