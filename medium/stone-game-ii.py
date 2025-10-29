class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @cache
        def stones(start, m, turn):
            if start >= len(piles):
                return 0, 0
            
            running_a, running_b = 0, 0
            ca, cb = -math.inf, -math.inf
            
            for i in range(start, min(start + 2 * m,  len(piles))):
                if turn:
                    running_a += piles[i]
                else:
                    running_b += piles[i]

                a, b = stones(i + 1, max(i - start + 1, m), not turn)

                alice = running_a + a
                bob = running_b + b

                
                if turn: 
                    if alice > ca:
                        ca = alice 
                        cb = bob
                    elif alice == ca and bob < cb:
                        cb = bob
                else:
                    if bob > cb:
                        ca = alice
                        cb = bob
                    elif bob == cb and alice < ca: 
                        ca = alice

            return ca, cb
                
        return stones(0, 1, True)[0]


            


