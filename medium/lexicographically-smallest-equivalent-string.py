from pprint import pprint

charmap = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

nummap = {charmap[k]: k for k in charmap}


class UnionFind:
    arr = []
    sizes = []
    min_chars = []

    def __init__(self, num):
        for i in range(num):
            self.arr.append(-1)
            self.sizes.append(1)
            self.min_chars.append(i + 1)

    def find(self, index):
        while self.arr[index] != -1:
            index = self.arr[index]

        return index

    def union(self, a, b):
        ind_a = self.find(a)
        ind_b = self.find(b)

        if ind_a == ind_b:
            return

        size_a = self.sizes[ind_a]
        size_b = self.sizes[ind_b]

        # merge smaller into larger
        if size_a < size_b:
            t = ind_b
            ind_b = ind_a
            ind_a = t

        self.sizes[ind_a] += self.sizes[ind_b]
        self.min_chars[ind_a] = min(self.min_chars[ind_a], self.min_chars[ind_b])
        self.arr[ind_b] = ind_a

    def get_min(self, index):
        index = self.find(index)
        return self.min_chars[index]


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        nummap = {charmap[k]: k for k in charmap}

        n = len(s1)
        uf = UnionFind(26)  # union find across characters
        uf.arr = [-1 for _ in range(len(uf.arr))]
        uf.sizes = [1 for _ in range(len(uf.arr))]
        uf.min_chars = [i + 1 for i in range(len(uf.arr))]

        for i in range(n):
            uf.union(charmap[s1[i]] - 1, charmap[s2[i]] - 1)

        res = ""
        for c in baseStr:
            min_char = uf.get_min(charmap[c] - 1)
            res += nummap[min_char]

        return res
