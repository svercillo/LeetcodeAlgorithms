class Solution:
    def numTilings(self, n: int) -> int:
        


        # nth state is in 3 possible states: straight line =1, missing top=2, missing bottom=3

        @cache
        def num_ways(index, state:int):
            nonlocal n
            if index == n:
                if state == 1:
                    return 1
                else:
                    return 0
            elif index > n -1:
                return 0

            
            nways = 0
            if state == 1:
                nways += num_ways(index + 1, 1) # one vertical
                nways += num_ways(index + 2, 1) # two horizontal
                nways += num_ways(index + 2, 2) # one bottom tromino
                nways += num_ways(index + 2, 3) # one top tromino

            elif state == 2: 
                nways += num_ways(index + 1, 1) # one top tromino
                nways += num_ways(index + 1, 3) # one horizontal domino on top


            elif state == 3: 
                nways += num_ways(index + 1, 1) # one bottom tromino
                nways += num_ways(index + 1, 3) # one horizontal domino on bottom

            return nways % (10 ** 9 + 7)

        
        return num_ways(0, 1)
