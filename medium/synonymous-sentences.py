class Solution:
    def generateSentences(self, syns: List[List[str]], text: str) -> List[str]:
        poss = set()
        for a, b in syns: 
            poss.add(a)
            poss.add(b)

        pmapping = {node: node for node in poss}
        groups = {node:[node] for node in poss}
        
        def parent(node):
            while pmapping[node] != node:
                node = pmapping[node]
        
            return node

        def union(a, b) :
            parenta = parent(a)
            parentb = parent(b)
            pmapping[parentb] = parenta

            for w in groups[parentb]:
                groups[parenta].append(w)

        for a, b in syns:
            union(a, b)


        pgroups = {
            node : sorted(groups[node]) for node in pmapping if node == parent(node)
        }
        print(pgroups)

        
        words = text.split(" ")
        ps =[]
        pgroup = []
        for w in words:
            if w in poss:
                ps.append(0)
                pgroup.append(parent(w))

        if not len(ps):
            return [text]
        

        def createtext():
            words = text.split()
            allws = []
            pind = 0
            for w in words:
                if w not in poss:
                    allws.append(w)
                else: 
                    # print(pind, pgroups[w], ps[pind])
                    allws.append(pgroups[parent(w)][ps[pind]])
                    pind += 1

            return " ".join(allws)
                    
                


        res = []
        valid = True
        while valid:

            t = createtext()
            res.append(t)
            ind = len(ps) -1
            ps[ind] += 1

            while ps[ind] == len(pgroups[pgroup[ind]]):
                ps[ind] = 0
                if ind == 0:
                    valid = False
                    break
                ind -= 1              
                ps[ind]  += 1



        return res
