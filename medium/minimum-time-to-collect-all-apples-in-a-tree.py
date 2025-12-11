class Solution:
    def minTime(self, n: int, edges: List[List[int]], apples: List[bool]) -> int:
        graph = defaultdict(set)
        for u, v in edges: 
            graph[u].add(v)
            graph[v].add(u)
        
        tree = defaultdict(set)
        visited = set()
        def constructtree(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited: 
                    tree[node].add(neigh)
                    constructtree(neigh)
        constructtree(0)

        @cache
        def hasapple(node): 
            if apples[node]:
                return True
            for neigh in tree[node]:
                if hasapple(neigh ):
                    return True
            return False

    
        count = 0
        @cache 
        def mintime(node):

            total = 0
            for neigh in tree[node]:
                print("\t" , neigh, hasapple(neigh))
                if hasapple(neigh):
                    total += mintime(neigh) + 2

            return total

        return mintime(0)

                
            


        

