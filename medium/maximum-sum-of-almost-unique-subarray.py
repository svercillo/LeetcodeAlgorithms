class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # sliding window

        n = len(nums)
        assert k <= n

        l, r = 0, k -1


        curr_sum = 0
        freq = {}
        for i in range(0, k):
            e = nums[i]
            if e not in freq:
                freq[e] = 0
            freq[e] += 1
            curr_sum += e

        

        _max = 0
        while r < n: 

            if len(freq) >= m:
                _max = max(_max, curr_sum)


            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                freq.pop(nums[l])

            
            curr_sum -= nums[l]
            l +=1
            r += 1


            
            if r < n:
                if nums[r] not in freq:
                    freq[nums[r]] = 0
                freq[nums[r]] += 1

        
                curr_sum += nums[r]

        return _max
