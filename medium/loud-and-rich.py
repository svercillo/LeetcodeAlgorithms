from functools import cache
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = defaultdict(lambda : set()) # richer than me

        for a, b in richer: 
            graph[b].add(a) # a is richer than b
        

        @cache
        def quietest_definitely_richer(node): # quietest person definitely richer
            # print(node, graph[node])
            loudest = quiet[node] # yourself as loudest
            loudest_node = node
            for richer in graph[node]: # iterate through all people richer than node
                quietness, quietest_node = quietest_definitely_richer(richer)
                if quietness < loudest:
                    loudest = quietness
                    loudest_node = quietest_node

            return loudest, loudest_node
        

        res = []
        for node in range(n): 
            _, quiet_node = quietest_definitely_richer(node)
            res.append(quiet_node)
        return res
