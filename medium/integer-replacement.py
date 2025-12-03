class Solution:
    def integerReplacement(self, n: int) -> int:
        
        q = [n]
        count = 0
        visited = set()
        while len(q):
            nq = []
            for e in q:
                if e == 1: 
                    return count
                visited.add(e)
                if e % 2 == 0:
                    if e // 2 not in visited: 
                        nq.append(e // 2)
                else:
                    if e + 1 not in visited:
                        nq.append(e +1)
                    if e -1 not in visited:
                        nq.append(e -1)
            q = nq
            count += 1

        return count


            

            


