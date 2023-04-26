class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        friends = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    friends.append((j, i))

        def calc_dist_from_axis_to_freinds(m, is_x:bool):
            
            total_dist = 0
            for x,y in friends:
                if is_x:
                    total_dist += abs(m - x)
                else:
                    total_dist += abs(m - y)

            return total_dist

        def calc_dist_from_point_to_freinds(px, py):
            total_dist = 0
            for x,y in friends:
                total_dist += abs(px - x)
                total_dist += abs(py - y)

            return total_dist

        def find_best_point(is_x:bool):
            nonlocal n, m
            end = math.inf
            l  = 0
            if is_x:
                end = m
            else:
                end = n

            r = end - 1
        
            while l <= r:

                m = (l + r) // 2
                

                left_dist = math.inf
                curr_dist = calc_dist_from_axis_to_freinds(m, is_x)
                right_dist = math.inf                

                if m > 0:
                    left_dist = calc_dist_from_axis_to_freinds(m-1, is_x)

                if m < end-1:
                    right_dist = calc_dist_from_axis_to_freinds(m+1, is_x)

                print(m, left_dist, curr_dist, right_dist)
                
                if left_dist >= curr_dist <= right_dist or left_dist == curr_dist or right_dist  == curr_dist:
                    return m
                elif left_dist <= curr_dist <= right_dist:
                    r = m - 1
                elif left_dist >= curr_dist >= right_dist:
                    l = m + 1
                else:
                    print("ERROR")
                    exit()

                
            return -math.inf


        x = find_best_point(is_x=True)
        y = find_best_point(is_x=False)
        print("best", x,y)
        
        print(x)

        res = calc_dist_from_axis_to_freinds(4, is_x=True)
        print(res)
        return calc_dist_from_point_to_freinds(x, y)
