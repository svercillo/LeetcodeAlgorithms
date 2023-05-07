from pprint import pprint
class UnionFind():
    def __init__(self, n):
        self.arr = [-1] * n
        self.sizes = [1] * n
        
    def find(self, a):
        while self.arr[a] != -1:
            a = self.arr[a]
        return a
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
        else:
            # merge 
            tup1, tup2 = sorted([(root_a, self.sizes[root_a]), (root_b, self.sizes[root_b])], key = lambda k : k[1])
            root_a, _ = tup1
            root_b, _ = tup2
            self.sizes[root_b] += self.sizes[root_a]
            self.arr[root_a] = root_b
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = [-1] * n
        
        uf = UnionFind(n)
        
        for i, j in pairs: 
            uf.union(i, j)
            
            
            
        info = {}
        
        # create reference objects
        for i, e in enumerate(uf.arr):
            if e == -1:
                chars = set()
                chars.add((s[i], i))

                info[i] = chars
            

        for i, e in enumerate(uf.arr):
            if e != -1:
                chars = info[uf.find(i)]
                chars.add((s[i], i))
        
    
        carr = [c for c in s]

        for i, e in enumerate(uf.arr):
            if e == -1:
                chars = info[uf.find(i)]
                letters = sorted([k[0] for k in chars])
                inds = sorted([k[1] for k in chars])
                
                print(letters, inds)
                for j in range(len(inds)):
                    carr[inds[j]] = letters[j]
                    
        res = ""
        
        for c in carr:
            res += c
            
        return res
                    
                
