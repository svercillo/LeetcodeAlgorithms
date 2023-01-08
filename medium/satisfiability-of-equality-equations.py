class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        graph = {}
 

        def find(source, target):
            if source in visited: 
                return False
            visited.add(source)
            if target in graph[source]:
                return True

            res = False
            for freind in graph[source]:
                res = res or find(freind, target)

            return res

        for string in equations:
            a = string[0]
            b = string[3]
            
            equals = string[1] == "="

            
            if a == b and not equals:
                return False

            if not equals:
                continue
        
            if a not in graph: 
                graph[a] = set()

            if b not in graph: 
                graph[b] = set()

            graph[a].add(b)
            graph[b].add(a)

        print(graph)

        for string in equations:
            a = string[0]
            b = string[3]
                        
            equals = string[1] == "="

            if equals:
                continue

            if a not in graph or b not in graph:
                continue
            visited = set()            
            if find(a, b):
                return False

        return True