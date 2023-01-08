class Node: 
    def __init__(self, qnt, expiry):
        self.qnt = qnt
        self.expiry = expiry
        
    def __lt__(self, other):
        return self.expiry < other.expiry
    
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        eaten = 0
        q = []
        n = len(apples)
        for i in range(n):
            # print(i, eaten)
            expiry = i + days[i]
            
            heapq.heappush(q, Node(apples[i], expiry))

            if len(q) > 0:
                while len(q) and i >= q[0].expiry:
                    heapq.heappop(q)
                    
                if len(q):
                    eaten += 1
                    node = heapq.heappop(q)
                    node.qnt -= 1
                    
                    if node.qnt > 0: 
                        heapq.heappush(q, node)

        i+=1
        while len(q):
            while len(q) and i >= q[0].expiry:
                heapq.heappop(q)

            if len(q):
                eaten += 1
                node = heapq.heappop(q)
                node.qnt -= 1

                if node.qnt > 0: 
                    heapq.heappush(q, node)
                
            i += 1
        
        return eaten
