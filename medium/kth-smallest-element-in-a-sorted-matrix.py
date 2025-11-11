from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        '''
        idea:
            n pointers 
            heap
        '''
        n = len(matrix)

        heap = []

        ps = [0] * n

        for pind in range(n):
            heappush(heap, (matrix[pind][0], pind))

        value = -9999
        while k:
            value, pind = heappop(heap)

            ps[pind] += 1

            if ps[pind] < n:
                heappush(heap, (matrix[pind][ps[pind]], pind))
            k -= 1

    
        return value 
            


        
