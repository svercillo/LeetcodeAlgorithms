class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        freq = dict(Counter(s))
        distinct = 0
        middle = ""


        poss = []
        for k, v in freq.items():
            if v % 2 == 1:
                distinct += 1
                middle = k
                poss += [k] * ((v-1) // 2 )
            else:
                poss += [k] * (v // 2)

        if n % 2 == 1:
            distinct -= 1
            
        if distinct > 0:
            return []



        
        def createprefix(poss, running, pre):
            if len(poss) == 0:
                pre.add("".join(running))
                return 

            for i in range(len(poss)):
                nposs=[]
                for j in range(len(poss)):
                    if i != j:
                        nposs.append(poss[j])
                
                nrunning = running.copy()
                nrunning.append(poss[i])

                createprefix(nposs, nrunning, pre)
        pre = set()
        createprefix(poss, [], pre)

        res = [
            p  + middle + p[::-1] for p in pre
        ]

        return res





