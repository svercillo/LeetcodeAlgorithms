class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        horizontal = set([0, m -1])
        vertical = set([0, n-1])

        vFences.sort()
        hFences.sort()

        hFences = [0] + [h -1 for h  in hFences] + [m-1]
        vFences = [0] + [v -1 for v in vFences] + [n-1]

        for h in hFences: 
            horizontal.add(h-1)

        for v in vFences:
            vertical.add(v -1)

        # print(hFences, vFences)

        vdiff_set = set()
        for i in range(len(vFences) -1): 
            for j in range(i + 1, len(vFences)):
                vstart = vFences[i]
                vend = vFences[j]
                # print(vstart, vend)
                vdiff_set.add(vend - vstart)


        # print(vdiff_set)
        largest_side = 0
        res = []
        for i in range(len(hFences) -1): 
            for j in range(i + 1, len(hFences)):
                hstart = hFences[i]
                hend = hFences[j]

                hdiff = hend - hstart
                if hdiff > largest_side and hdiff in vdiff_set:

                    largest_side = hdiff
                    
            
        return pow(largest_side, 2, 10 ** 9 + 7) if largest_side != 0 else -1
