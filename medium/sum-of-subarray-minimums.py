class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 +7
        res = sum(arr)
        n = len(arr)

        res = 0
        running = 0
        minsub = defaultdict(int)
        heap = []
        for i,e in enumerate(arr):
            totalending = 1
            while len(heap) and e <= heap[-1]:

                last = heap.pop()
                totalending += minsub[last]
                running -= minsub[last] * last
                minsub.pop(last)

            running += totalending * e
            minsub[e] = totalending
            heap.append(e)
 
            res += running % MOD

            res %= MOD
 
        return res
            
            
            





            

        

