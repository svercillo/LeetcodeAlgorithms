from pprint import pprint

class Node:
    def __init__(self, value, wind):
        self.value = value
        self.neighs = {}
        self.wind = wind
        self.lwind = wind


class Trie:
    def __init__(self):
        self.head = Node("_", -1)

    def addword(self, word, wind):
        node = self.head 

        for c in word: 
            if c not in node.neighs:
                node.neighs[c] = Node(c, wind)
                node = node.neighs[c]
            else: 
                node = node.neighs[c]
                node.lwind = wind

        if len(node.neighs) > 0: 
            return False

        return True


    def creategraph(self):
        q = [self.head]
        graph = defaultdict(set)
        revgraph = defaultdict(set)
        while len(q):
            nq = []
            for node in q:
                for c1 in node.neighs: # 26 * 26 worst case
                    for c2 in node.neighs:
                        if c1 == c2:
                            continue
                    
                        n1 = node.neighs[c1]
                        n2 = node.neighs[c2]

                        if n1.wind < n2.wind:

                            if n2.wind < n1.lwind:
                                print("SDFSDFSDF")
                                return None, None
                            graph[c1].add(c2)
                            revgraph[c2].add(c1)

                    nq.append(node.neighs[c1])
            q = nq

        return graph,revgraph


        


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def createalpha(words): 
            alpha = set()
            for w in words:
                for c in w:
                    alpha.add(c)
            return alpha

        def getindeg0(revgraph, alpha):
            res = [] 
            for c in alpha:
                if c not in revgraph:
                    res.append(c)
            return res

        alpha = createalpha(words)
        trie = Trie()
        for wind, w in enumerate(words): 
            if not trie.addword(w, wind):
                print("invalid ordering")    
                return ""

        graph,revgraph = trie.creategraph()
        if graph is None:
            print("invalid cycle1")
            return "" 
        indeg0 = getindeg0(revgraph, alpha)


    
        print("graph")
        pprint(dict(graph))
        pprint(dict(revgraph))

        print(indeg0)


        res = []
        q = indeg0
        covered = set()
        while len(q):
            nq = []
            for node in q:
                covered.add(node)
                res.append(node)

                for neigh in graph[node]:
                    if node in revgraph[neigh]:
                        revgraph[neigh].remove(node)
                    
                    if not len(revgraph[neigh]):
                        nq.append(neigh)
            q = nq
        
        for c in alpha:
            if c not in covered:
                print("graph cycle")
                return "" 

        return "".join(res)        


        

