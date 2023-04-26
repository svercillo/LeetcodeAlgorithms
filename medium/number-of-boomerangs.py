class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def calc_distance(p1, p2):
            return (
                (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            ) ** 0.5

        total = 0
        for i, (i1, j1) in enumerate(points):
            dist_freq = {}
            for j, (i2, j2) in enumerate(points):
                if i == j:
                    continue

                dist = calc_distance((i1, j1), (i2, j2))

                # print((i1, j1), (i2, j2), dist)
                if dist in dist_freq:
                    total += dist_freq[dist] * 2
                
                    dist_freq[dist] += 1
                else:
                    dist_freq[dist] = 1

            # print(i, dist_freq)

        return total

