class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        values = []
        for i, e in enumerate(nums):
            values.append((e,i))

        values.sort(key = lambda k : k[0])

        earliest = math.inf
        latest = -math.inf

        for ind, (e, i) in enumerate(values):
            print(ind, (e, i))
            if ind > i:
                earliest = min(i, earliest)
                
            elif ind < i:
                latest = max(i, latest)
                
                
        if earliest == math.inf:
            return 0

        return latest - earliest + 1
