class Combiner:
    def __init__(self, n):
        self.n = n
        self.pmapping = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def findparent(self, node):
        pmapping = self.pmapping
        
        while pmapping[node] != node:
            node = pmapping[node]

        return node
    
    def union(self, a, b):
        parenta = self.findparent(a)
        parentb = self.findparent(b)

        if parenta == parentb:
            return False

        if self.size[parenta] >= self.size[parentb]: 
            # join into a
            self.pmapping[parentb] = parenta
            self.size[parenta] += self.size[parentb]
        else:
            # join into b
            self.pmapping[parenta] = parentb
            self.size[parentb] += self.size[parenta]
            
        return True
    
    def smallestingroup(self, node):
        parent = findparent(node)
        return self.size[parent]
    


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = c + 1
        dsu = Combiner(n)
        for a, b in connections:
            dsu.union(a, b)


        heaps = defaultdict(list)

        for node in range(n):
            parent = dsu.findparent(node)
            heapq.heappush(heaps[parent], node)

        # print(heaps)
        res = []
        offline = [False] * n
        for t, x in queries:
            # print(offline, heaps)
            if t == 2:
                offline[x] = True
            elif not offline[x]:
                res.append(x)
            else:
                parent = dsu.findparent(x)
                h = heaps[parent]

                # print("SDFSDF", h[0], offline[h[0]])
                while len(h) and offline[h[0]]:
                    # print("hsdfsdf")
                    heapq.heappop(h) # pop invalid

                if not len(h):
                    res.append(-1)
                else:
                    res.append(h[0])

        print(res)
        return res
                

                
