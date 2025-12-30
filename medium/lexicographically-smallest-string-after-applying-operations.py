class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def applya(s):
            carr = []
            for i,c in enumerate(s): 
                d = int(c)
                if i % 2 ==  1:
                    d = (int(c) + a) % 10
                carr.append(str(d))
            return "".join(carr)

        def applyb(s):
            carr = []
            for i in range(len(s)):
                carr.append(s[(i + b) % len(s)])
            return "".join(carr)

        visited = set()

        q = [s]
        while len(q):
            nq = []
            for s in q:
                na_s = applya(s)
                nb_s = applyb(s)

                # print(s, " ->  ", na_s )
                # print(s, " ->  ", nb_s)

                if na_s not in visited:
                    nq.append(na_s)
                    visited.add(na_s)

                if nb_s not in visited:
                    nq.append(nb_s)
                    visited.add(nb_s)
            q = nq

        smallest = "9" * len(s)
        for s in visited:
            if int(s) < int(smallest):
                smallest = s

        return smallest




            
            







            

