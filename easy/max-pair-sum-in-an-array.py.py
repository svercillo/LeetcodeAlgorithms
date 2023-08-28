class Solution:
    def maxSum(self, nums: List[int]) -> int:

        
        groupings = []
        for i in range(0, 10): 
            groupings.append([])
        
        for e in nums: 
            mdigit = -1
            for c in str(e): 
                mdigit = max(int(c), mdigit)
            groupings[mdigit].append(e)

    
        print(groupings)
        res = -1
        for i in range(1, 10):
            
            _max = -math.inf
            _sec_max  = -math.inf

            for e in groupings[i]:
                if e > _max:
                    _sec_max = _max
                    _max = e

                elif e > _sec_max:
                    _sec_max = e

            res = max(_max + _sec_max, res)

        return res

            
