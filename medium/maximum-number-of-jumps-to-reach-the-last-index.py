class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # jump from i to j  ( j > i), if abs(nums[j] - nums[i]) <= target
        

        # easy: map all the indexes from i to set(ind_can_jump_to)


        can_jump_to = []
        n = len(nums)
        for i in range(n):

            inds = []
            for j in range(i+ 1, n):
                if abs(nums[i] - nums[j]) <= target:
                    inds.append(j)
            can_jump_to.append(inds)

        print(can_jump_to)
        

        @cache 
        def maxJumps(i):
            nonlocal n
            possible = []
            if i == n -1:
                return 0

            
            for ind in can_jump_to[i]:
                res = maxJumps(ind)
                if res < 0:
                    continue
                possible.append(res+ 1)

            if not len(possible): 
                return -math.inf

            return max(possible)




        _max = maxJumps(0)

        

        return _max if _max > 0 else -1