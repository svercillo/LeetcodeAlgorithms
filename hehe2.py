from functools import cache
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2.sort()
        def get_largest_element_smaller_than_x(arr, x):
            n = len(arr)
            lp, rp = 0, n - 1

            while lp <= rp: 
                m = (lp+rp) // 2

                if arr[m] < x:
                    lp = m + 1
                else:
                    rp = m - 1
            
            def check_index(ind):
                if not (0 <= ind < len(arr)): return False
                if arr[ind] < x and (ind + 1 == len(arr) or  arr[ind + 1] >= x):
                    return True
            
            if lp == n:
                lp -= 1
            
            if check_index(lp): return lp
            if check_index(lp + 1): return lp + 1
            if check_index(lp - 1): return lp -1

            return -1
            
        # @cache
        def recurse(ind, last_ele):
            if ind == -1:
                print("Sdfsdfsdf")
                return 0
            
            n2 = len(arr2)

            largest_ind = get_largest_element_smaller_than_x(arr2, arr1[ind])

            if largest_ind == -1: # can't perform operation
                if arr1[ind] < last_ele:
                    res =  recurse(ind -1, arr1[ind])
                else: # can't perform operation, can't keep index
                    print("CANT DO ANYTHING", arr1[ind], last_ele)
                    res =  math.inf  

            else:
                if arr1[ind] < last_ele:
                    res = min(
                        recurse(ind -1, arr1[ind]), # don't perform operation
                        recurse(ind -1, arr2[largest_ind]) + 1 # perform operation (add 1)
                    )
                else:
                    # must perform operation
                    res = recurse(ind -1, arr2[largest_ind]) + 1

            print(ind, last_ele, res)
            return res
        
        return recurse(len(arr1) - 1, math.inf) 



