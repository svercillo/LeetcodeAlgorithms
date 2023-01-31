# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        l, r = 0, n - 2


        while l <= r: 
            m = (l+r) // 2

            if mountain_arr.get(m) > mountain_arr.get(m+1): 
                r = m - 1 
            else:
                l = m + 1



        peak_ind = l 

        if mountain_arr.get(peak_ind) == target:
            return peak_ind

        

        def binary_search(l, r, increasing):
            
            while l <= r:
                m = (l+r) // 2

                value = mountain_arr.get(m)
                if value == target:
                    return m

                if increasing:
                    if value > target:
                        r = m -1
                    else:
                        l = m +1
                else:
                    if value < target:
                        r = m -1
                    else:
                        l = m +1
            return -1

        
        # check increasing arr
        l, r = 0, peak_ind-1
        res1 = binary_search(l, r, increasing=True)

        if res1 != -1:
            return res1

        l, r = peak_ind+1, n -1
        res2 = binary_search(l, r, increasing=False)

        if res2 != -1:
            return res2

        return -1
