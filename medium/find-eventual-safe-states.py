class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        @cache
        def isSafe(node):
            if node in seen:
                return False
            
            seen.add(node)
            
            invalid = False
            for neigh in graph[node]:
                if not isSafe(neigh):
                    invalid = True
            seen.remove(node)
            return not invalid

        res = [] 
        for node in range(len(graph)):
            seen = set()
            if isSafe(node):
                res.append(node)


        return res
