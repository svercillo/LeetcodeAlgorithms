class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set([tuple([int(e) for e in array]) for array in deadends])
        q = [[0,0,0,0]] 

        target = tuple([int(e) for e in target])

        visited = set()
        count = 0
        while len(q):
            nq = []
            for array in q:
                string = tuple(array)

                if string == target:
                    return count                

                
                if string in visited or string in ends:
                    continue
                visited.add(string)

                for i in range(4):
                    e = array[i]

                    incr = array.copy()
                    incr[i] += 1
                    incr[i] %= 10

                    decr = array.copy()
                    decr[i] += 10 - 1
                    decr[i] %= 10

                    nq.append(incr)
                    nq.append(decr)

            count += 1
            q = nq
        

        return -1
