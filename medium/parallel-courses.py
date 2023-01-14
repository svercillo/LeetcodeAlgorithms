class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(lambda : set()) # for course k, it has [v for v in vals] as prereq

        for prereq, req in relations:
            graph[req].add(prereq)

        visited = {}
        def longest_dist(node, path_contains):
            if node in visited:
                return visited[node]
            if node in path_contains:
                return math.inf
            path_contains.add(node)

            if len(graph[node]) == 0:
                return 1
            
            mdist = 0
            for prereq in graph[node]:
                mdist = max(longest_dist(prereq, path_contains) + 1, mdist)


            visited[node] = mdist
            return mdist

        mdist = 0
        for course in range(1, n+1):
            mdist = max(longest_dist(course, set()), mdist)

        return mdist if mdist != math.inf else -1
