class UnionFind:
    def __init__(self, n):
        self.arr, self.sizes = [], []
        for i in range(n):
            self.arr.append(-1)
            self.sizes.append(1)

    def find(self, a):
        while self.arr[a] != -1:
            a = self.arr[a]
        return a

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return
        else:  # merge smaller set into larger set
            if self.sizes[root_b] > self.sizes[root_a]:  # 'a' is larger set
                t = root_b
                root_b = root_a
                root_a = t

            self.sizes[root_a] += self.sizes[root_b]
            self.arr[root_b] = root_a

    def get_set_size(self, a):
        return self.sizes[self.find(a)]


class Solution:
    def earliestAcq(self, logs, n: int) -> int:
        logs.sort(key=lambda k: k[0])

        uf = UnionFind(n)
        for time, a, b in logs:
            currtime = time
            uf.union(a, b)
            if uf.get_set_size(a) == n or uf.get_set_size(a) == n:
                return currtime

        return -1
