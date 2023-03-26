class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum([p for p in piles])

        piles = deque(piles)
        
        cache = {}
        def maxscore(piles, alices_turn):
            if len(piles) == 0:
                return 0

            if (tuple(piles), alices_turn) in cache:
                return cache[(tuple(piles), alices_turn)]

                
            front = piles[0]
            back = piles[-1]

            front_pile = piles.copy()
            front_pile.popleft()

            back_pile = piles.copy()
            back_pile.pop()


            if alices_turn:
                res = max(
                    maxscore(front_pile, False) + front,
                    maxscore(back_pile, False) + back
                )

            else:
                res = max(
                    maxscore(front_pile, True),
                    maxscore(back_pile, True)
                )

            cache[(tuple(piles), alices_turn)] = res

            return res

            


        m_score = maxscore(piles, True)
        
        return  m_score > total / 2
            
