import heapq

class Node:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [Node(stone) for stone in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:

            top = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if top.val > second.val:
                heapq.heappush(heap, Node(top.val - second.val))

        if len(heap): 
            return heap[0].val
        return 0

