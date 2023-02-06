class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        
        heapq.heapify(gifts)

        while k:
            top = heapq.heappop(gifts)
            
            heapq.heappush(gifts, math.ceil(-(-top) ** 0.5))
            k -=1
            
        return - sum(gifts)
    
