import heapq

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        
        _max = max(nums)
        n = len(nums)
        hp = [(_max - e, i) for i, e in enumerate(nums[:k-1])]
        heapq.heapify(hp)


        res = []
        for i in range(k-1, n):
            heapq.heappush(hp,(_max - nums[i], i))

            while len(hp) and hp[0][1] <= i - k:
                heapq.heappop(hp)

            res.append(_max - hp[0][0])

        return res
            
