
class Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        n = len(s)

        graph = []
        for _ in range(n):
            graph.append([])

        for i, parent in enumerate(parents):
            if parent == -1:
                continue
            graph[parent].append(i)
            

        def dfs(node):
            
            longest = 0
            second_longest = 0

            longest_prev_comb = 0
            for neigh in graph[node]:
                prev_comb, length = dfs(neigh)
                longest_prev_comb = max(longest_prev_comb, prev_comb)
                if s[neigh] == s[node]:
                    continue

                

                if length >= longest:
                    second_longest = longest
                    longest = length
                elif length > second_longest:
                    second_longest = length



            res1, res2 = max(longest_prev_comb, longest + second_longest + 1), longest +1
            return res1, res2

        return max(dfs(0))
