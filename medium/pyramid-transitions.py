from pprint import pprint
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        amap = defaultdict(list)
        for s in allowed:
            l, r, t = s 
            amap[(l,r)].append(t)
        # pprint(dict(amap))
        q = [bottom]
        while len(q) and len(q[0]) > 1:
            nq = []

            for bottom in q:
                clevel = []
                invalid = False
                for i in range(len(bottom) -1):
                    l, r = bottom[i], bottom[i+1]

                    tops = amap[(l,r)]
                    if not len(clevel):
                        clevel = tops
                    else:
                        nclevel = []
                        for pre in clevel:
                            for t in tops:
                                nclevel.append(pre + t)

                        if not len(nclevel):
                            invalid = True
                            break

                        clevel = nclevel


                if invalid or (len(clevel) and len(bottom) -  len(clevel[0]) > 1):
                    continue
                for s in clevel:
                    nq.append(s)

            # print(nq)
            q = list(set(nq))

                                
        # print('HERE', q)

        
        return bool(len(q) and len(q[0]) == 1)
            

        
