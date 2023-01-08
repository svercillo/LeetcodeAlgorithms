class Solution:
    def findMinArrowShots(self, points) -> int:

        if len(points) == 0:
            return 0

        points.sort(key=lambda x: x[0])

        print(points)
        num_arrows = 1
        largest = points[0][1]

        for x1, x2 in points:
            if x1 <= largest:
                if x2 < largest:
                    largest = x2
            else:
                print(x1, x2)
                num_arrows += 1
                largest = x2

        return num_arrows
