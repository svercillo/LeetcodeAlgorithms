class Solution:
    class Node:
        def __init__(self, ind, val):
            self.ind = ind
            self.val = val
        
        def __lt__(self, other):
            return self.val < other.val

        def __repr__(self) -> str:
            return f"{self.val}"

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # classic sliding window

        n = len(nums)
        lp,rp = 0, 0

        min_heap = []
        max_heap = []

        largest = 1
        # heapq.heappush(max_heap, self.Node(rp, -nums[rp]))
        # heapq.heappush(min_heap, self.Node(rp, nums[rp]))
        while rp < n:        
            heapq.heappush(max_heap, self.Node(rp, -nums[rp]))
            heapq.heappush(min_heap, self.Node(rp, nums[rp]))
            
            # print(max_heap, min_heap)
            while -max_heap[0].val - min_heap[0].val > limit:
                while min_heap[0].ind < lp:
                    heapq.heappop(min_heap)

                while max_heap[0].ind < lp:
                    heapq.heappop(max_heap)
                
                if -max_heap[0].val - min_heap[0].val > limit: 
                    lp += 1

            # print(max_heap, min_heap, lp, rp)
            if rp - lp + 1 > largest:
                largest = rp - lp + 1

            rp += 1



        return largest
