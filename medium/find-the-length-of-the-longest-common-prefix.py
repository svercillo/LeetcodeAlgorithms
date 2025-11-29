class Trie:
    def __init__(self, words):
        self.root = {}
        for w in words:
            self.insert(str(w))

    def insert(self, word):

        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["*"] = True

    def lcprefix(self, word):
        word = str(word)

        node = self.root
        for i, c in enumerate(word):
            if c not in node:
                return i
            node = node[c]
        
        return len(word)
    

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        n1, n2 = len(arr1), len(arr2)
        if n1 < n2:
            t = arr1 
            arr1 = arr2
            arr2 = t

        trie = Trie(arr2)
        msz = 0
        for w in arr1:
            sz = trie.lcprefix(w)

            msz = max(sz, msz)

        return msz
