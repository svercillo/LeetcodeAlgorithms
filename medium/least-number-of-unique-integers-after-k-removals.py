import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        class Node:
            def __init__(self, number, count):
                self.number = number
                self.count = count
                self.duplicate = False

            def __lt__(self, other):
                return self.count < other.count

        freq = {}

        for e in arr:
            if e not in freq:
                freq[e] = 0
            freq[e] += 1


        heap = []
        for e in freq:
            heapq.heappush(heap, Node(e, freq[e]))


        while k > 0 and len(heap):
            while len(heap) and heap[0].duplicate:
                heapq.heappop(heap)
                
            if k >= heap[0].count:
                top:Node = heapq.heappop(heap)
                
            else:
                top:Node = heap[0]
                top.duplicate = True

                new_node = Node(top.number, top.count - k)
                heapq.heappush(heap, new_node)

            k -= top.count

        count = 0
        for node in heap:
            if not node.duplicate:
                count += 1

        return count
