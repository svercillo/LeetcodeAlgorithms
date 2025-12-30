from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fq = []
        q = []
        freq = Counter(tasks)
        
        for t in freq:
            heappush(q,  (-freq[t], t))

        # # print(q)
    

        curr = 0
        while len(fq) or len(q): 
            if not len(q):
                curr = fq[0][0]
            
            while len(fq) and fq[0][0] <= curr:
                _, f, t = heappop(fq)
                heappush(q, (f,t ))

            f, t = heappop(q)            
            if abs(f) > 1:
                heappush(fq, (curr + n+1, f+1, t))

            # print(t, curr)
            curr += 1

            # print(q, fq, curr)
            

        return curr 
            


