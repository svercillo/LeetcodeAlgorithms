class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:


        n = len(nums)
        
        last_odd_ind = -1
        last_even_ind = -1

        nxt_even_inds = [-1]  * n
        nxt_odd_inds = [-1] * n
        i = n - 1 
        while i >= 0:
            nxt_even_inds[i] = last_even_ind
            nxt_odd_inds[i] = last_odd_ind

            if nums[i] % 2 == 0:
                last_even_ind = i
            else:
                last_odd_ind = i
            i -= 1



        print(nxt_even_inds)
        print(nxt_odd_inds)
        @cache
        def getMax(i):
            nxt_even_ind = nxt_even_inds[i]
            nxt_odd_ind = nxt_odd_inds[i]

            possible = []
            if nxt_even_ind != -1:
                if nums[i] % 2 == 0:
                    possible.append(getMax(nxt_even_ind) + nums[i])
                else:
                    possible.append(getMax(nxt_even_ind) + nums[i] - x)
            
            if nxt_odd_ind != -1:
                if nums[i] % 2 == 0:
                    possible.append(getMax(nxt_odd_ind) + nums[i] -x)
                else: 
                    possible.append(getMax(nxt_odd_ind) + nums[i])

            possible.append(nums[i])
            return max(possible)
                

            
            
        return getMax(0)
