class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        # last_pos is up 1 or down 0
        @cache
        def min_swaps(ind, number, last_pos):
            if ind == len(tops):
                return 0
                
            if number == tops[ind] == bottoms[ind]:
                return min_swaps(ind + 1, number, last_pos)
            elif number == tops[ind]:
                if last_pos == 1:
                    res = min_swaps(ind +1, number, 1) # dont need to swap 
                else:
                    res = min_swaps(ind +1, number, 0) + 1 # need to swap
            elif number == bottoms[ind]:
                if last_pos == 0:
                    res = min_swaps(ind +1, number, 0) # dont need to swap 
                else:
                    res = min_swaps(ind +1, number, 1) + 1 # need to swap
            else:
                return math.inf # impossible

            return res
        
        n_swaps = math.inf
        for num in range(1,7):
            res1 = min_swaps(0, num, 1)
            res2 = min_swaps(0, num, 0)

            if res1 != -1:
                n_swaps = min(res1, n_swaps)

            if res2 != -1:
                n_swaps = min(res2, n_swaps)

        

        return n_swaps if n_swaps != math.inf else - 1
