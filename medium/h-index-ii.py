class Solution:
    def hIndex(self, nums : List[int]) -> int:
        
        '''
        intuition: 
            h index as a funciton of (ind) strict ascending then decending
            binary search inflection point
        '''

        n = len(nums)
        l,r = 0, n 


        if n <2: 
            return min(min(nums), n)

        def hindex(ind):
            if ind >= n:
                return 0
            ncit = nums[ind] 
            npapers = n - ind
            return min(npapers, ncit)

        while l < r: 
            m = (l +r) // 2
            m2 = m + 1

            if m2 == n:
                incr = False
            else:
                h1 = hindex(m)
                h2 = hindex(m2) 

                incr = h2 >= h1

            if incr: 
                l = m + 1

            else:
                r = m    
        return max(hindex(l), hindex(l+1))
