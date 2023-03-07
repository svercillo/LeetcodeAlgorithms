from collections import defaultdict
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:    
        # factor_map = defaultdict(lambda : ) # factor to group indicator     
        def get_factors(num):
            res = set()
            for i in range(2, int(num** 0.5) + 1):
                if num % i == 0:
                    res.add(i)
                    res.add(num // i)
            if num != 1:
                res.add(num)
            return res

        n = len(nums)
        ss = 1
        suffix = defaultdict(lambda : 0)
        for i in range(0, n):
            for f in get_factors(nums[n-1 -i]):
                suffix[f] += 1
            ss *= nums[i]

        prefix = defaultdict(lambda : 0)
        shared = set()
        pp = 1
        
        for i in range(n-1):
            pp *= nums[i]
            ss //= nums[i]
            for f in get_factors(nums[i]):
                suffix[f] -= 1
                if suffix[f] == 0:
                    suffix.pop(f)
                    if f in shared: 
                        shared.remove(f)
                prefix[f] += 1
                if f in suffix:
                    shared.add(f)

            if len(shared) == 0:
                return i

        return -1
