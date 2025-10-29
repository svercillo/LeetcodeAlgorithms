class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        

        n = len(nums)
        def xSum(nums): # start end inclusiv 
            nonlocal n 
            freq = {}

            for e in nums: 
                if e not in freq:
                    freq[e] = 0
                freq[e] += 1


            valuePairs = [(e, freq[e]) for e in freq]
            valuePairs.sort(key = lambda k : (k[1], k[0]), reverse=True)

            _sum = 0
            for i in range(min(len(valuePairs), x)):
                _sum += valuePairs[i][0] * valuePairs[i][1]

            
            return _sum
            


        res = []
        for i in range(n - k + 1):
            res.append(xSum(nums[i : i +k]))


        return res



