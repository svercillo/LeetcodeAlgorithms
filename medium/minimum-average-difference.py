class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        prefix = []
        presum = 0
        for e in nums:
            presum += e
            prefix.append(presum)

        
        totalsum = prefix[-1]


        min_avg = math.inf
        min_ind = -1
        for i in range(n):
            pre = prefix[i] // (i+1)
            post = (totalsum - prefix[i]) // (n - i - 1) if i < n-1 else 0 

            if abs(pre- post) < min_avg:
                min_ind = i
                min_avg = abs(pre -post)

            

        return min_ind


