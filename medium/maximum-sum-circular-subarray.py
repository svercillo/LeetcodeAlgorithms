class Solution(object):
    def maxSubarraySumCircular(self, A):
        n = len(A)

        prefix = []
        presum = 0
        diff = -math.inf

        for i in range(2):
            for e in A:
                presum += e
                prefix.append(presum)
                if i == 0:
                    diff = max(diff, presum)

        n = len(A)
        
        print(prefix)
        smallest = 0
        smallest = math.inf
        smallest_ind = 0

                
        
        smallest_arr = [-1] * len(prefix)
        dq = deque()
        for i in range(len(prefix)):
            if len(dq) == 0 :
                dq.append((prefix[i], i))
            else:
                # evict from left baesd on index OOB 
                while len(dq) and i - dq[0][1] > n:
                    dq.popleft()                
                

                
                # evict from right based on value
                while len(dq) and prefix[i] < dq[-1][0]: 
                    dq.pop()

                dq.append((prefix[i],i))



            smallest_arr[i] = dq[0]


        diff = -math.inf
        for i in range(len(prefix)):
            if smallest_arr[i][1] != i:
                diff = max(diff, prefix[i] - smallest_arr[i][0])

        
        return max(diff, max(A)) 
