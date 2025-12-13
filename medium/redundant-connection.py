class Dsu:
    def __init__(self,n):
        self.n = n
        self.pmapping = {i : i for i in range(n+ 1)}
        self.size = {i: 1 for i in range(n +1)}

    def parent(self, node):
        while self.pmapping[node] != node:
            node = self.pmapping[node]

        return node

    def union(self, a, b ): 
        parenta = self.parent(a)
        parentb = self.parent(b)

        if self.size[parenta] >= self.size[parentb]:
            self.pmapping[parentb] = parenta
            self.size[parenta] += self.size[parentb]
        else:
            self.pmapping[parenta] = parentb
            self.size[parentb] += self.size[parenta]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max([max(a,b) for a, b in edges])

        dsu = Dsu(n)
        for a, b in edges:
            parenta = dsu.parent(a)
            parentb = dsu.parent(b)

            if parenta == parentb:
                return [a, b]

            dsu.union(a, b)
        
