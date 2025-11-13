class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:


        def findnearest(array, target):
            n = len(array)

            l, r = 0, n
            while l < r:
                m = (l+r )// 2
                if array[m] < target:
                    l = m+1
                else:
                    r = m
        
            smallest = []
            if l < n:
                smallest.append(abs(target - array[l]))
            if l + 1 < n:
                smallest.append(abs(target - array[l+1]))
            if l -1 >= 0:
                smallest.append(abs(target - array[l-1]))
            return min(smallest)

        queues = defaultdict(list)
        for i,c in enumerate(colors):
            queues[c].append(i)
        


        res = []
        for ind, c in queries: 
            indarray = queues[c] 
        
            if len(indarray) == 0:
                res.append(-1)
            else:
                res.append(findnearest(indarray, ind))

        return res

            

        
