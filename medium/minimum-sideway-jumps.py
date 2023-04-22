class Solution:
    def minSideJumps(self, obstacles) -> int:
        
        dp = [] 
        for i in range(len(obstacles)):
            dp.append([-1, -1, -1])

        def min_side_jumps(ind, lane):
            if ind == len(obstacles):
                return 0

            if dp[ind][lane] != -1:
                return dp[ind][lane]

            if ind > 0 and obstacles[ind -1] - 1 == lane:
                return math.inf
            
            if obstacles[ind]-1 == lane:
                return math.inf  # impossible: hit obstacle

            min_num_jumps = math.inf

            min_num_jumps = min(
                min_num_jumps,
                min_side_jumps(ind+ 1, lane)
            )

            min_num_jumps = min(
                min_num_jumps,
                min_side_jumps(ind+1, (lane + 1) % 3) + 1
            )

            min_num_jumps = min(
                min_num_jumps,
                min_side_jumps(ind+1, (lane + 2) % 3) + 1 
            )


            dp[ind][lane] = min_num_jumps
            return min_num_jumps

        return min_side_jumps(0, 1)
