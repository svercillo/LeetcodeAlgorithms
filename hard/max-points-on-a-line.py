from collections import defaultdict
class Solution:
    def maxPoints(self, points):
        if not points:
            return 0

        max_count = 1
        for i in range(len(points)):
            slopes = defaultdict(int)
            same_points = 1
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    same_points += 1
                    continue
                elif x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                slopes[slope] += 1
            max_count = max(max_count, same_points)
            for count in slopes.values():
                max_count = max(max_count, count + same_points)
        return max_count