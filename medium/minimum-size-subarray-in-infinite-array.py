class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        prefix = []
        presum = 0

        for e in nums + nums:
            presum += e 
            prefix.append(presum)

        total_sum = sum(nums)
        num_rounds = 1
        if target % total_sum == 0:
            return target // total_sum * len(nums)
        num_rounds = target // total_sum
        target %= total_sum 

        premap = {}
        shortest = math.inf

        for i, e in enumerate(prefix):
            print()
            if e == target:
                print("SDFSDF")
                shortest = min(i+1, shortest+ 1) 
            if e - target in premap:
                shortest = min(shortest, i - premap[e- target])

            premap[e] = i

        shortest += num_rounds * len(nums)
        return shortest if shortest != math.inf else -1

        
