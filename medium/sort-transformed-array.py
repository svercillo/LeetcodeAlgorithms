class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x, a, b,c):
            return (a * x * x) + (b * x) + c


        if a == 0:
            if b >= 0:
                return [quadratic(x, a, b, c) for x in nums] 

            else:
                return [quadratic(x, a, b, c) for x in nums[::-1]] 
        
        x_inflection_point = -b / 2 / a        
        

        gte_ind = -1
        for i, x in enumerate(nums):
            if x >= x_inflection_point:
                gte_ind = i
                if i == 0:
                    return nums # edge case
 
                break

        if gte_ind == -1:
            return nums[::-1] # edge case 
        
        n = len(nums)
        if nums[gte_ind] == x_inflection_point: 
            l, r = gte_ind, gte_ind
            
        else:
            l, r = gte_ind - 1, gte_ind

            # res = []
            # if l >= 0: 
            #     res.append(nums[l])
            # res.append(gte_ind)
            


        print("gte_ind",gte_ind, x_inflection_point)
        res = []

        while l >=0 or r < n:
            lval = nums[l] if l >= 0 else math.inf
            rval = nums[r] if r < n else math.inf

            if abs(lval - x_inflection_point) < abs(rval - x_inflection_point):

                res.append(nums[l])
                l -= 1
            else:
                if r != l:
                    res.append(nums[r])
                r += 1



        if a < 0:
            res = res[::-1]


        
        print([quadratic(x, a, b, c) for x in res])


        return [quadratic(x, a, b, c) for x in res] 
        
            
