class Solution:
    def answerQueries(self, nums: List[int], qs: List[int]) -> List[int]:

        n = len(nums)
        m = len(qs)

        result = [0] * m
        queries = []
        for i, e in enumerate(qs):
            queries.append((e, i))
        
        nums.sort()
        queries.sort(key =lambda k : k[0])

        prefix = []
        presum = 0
        for e in nums:
            presum += e
            prefix.append(presum)

        nind = 0
        qind = 0
        while qind < m:
            while nind < n and prefix[nind] <= queries[qind][0]:
                nind += 1

            ind = queries[qind][1]
            result[ind] = nind

            qind += 1
        

        return result
