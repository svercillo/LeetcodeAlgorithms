class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digs = str(n)

        
        res = []

        def recurse(possible, running):
            if len(running) and running[0] == '0':
                return False
            
            if len(possible) == 0:
                # print(running, possible)

                if running[0]  == '0':
                    return False

                value = int("".join(running))
                if 0 <= (log(value) / log(2)) % 1 < 0.00000001:
                    return True
                return False

            for i, d in enumerate(possible):
                nrunning = running.copy()
                nrunning.append(d)

                npossible = [e for j, e in enumerate(possible) if  j != i]
                
                if recurse(npossible, nrunning):
                    return True
            return False                


        return recurse(digs, [])
