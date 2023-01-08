class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):

        slots1.sort(key=lambda k: k[0])
        slots2.sort(key=lambda k: k[0])
        n = len(slots1)
        m = len(slots2)

        p1, p2 = 0, 0

        while p1 < n and p2 < m:

            # if overlap
            if slots1[p1][1] > slots2[p2][0] and slots2[p2][1] > slots1[p1][0]:

                start = max(slots1[p1][0], slots2[p2][0])
                end = min(slots1[p1][1], slots2[p2][1])


                overlap = end - start
                if overlap >= duration:
                    return [start, start + duration]

                if slots1[p1][1] >= slots2[p2][1]:
                    p2 += 1
                else:
                    p1 += 1
            else:
                if slots2[p2][0] > slots1[p1][0]:
                    p1 += 1
                else:
                    p2 += 1
        return []
