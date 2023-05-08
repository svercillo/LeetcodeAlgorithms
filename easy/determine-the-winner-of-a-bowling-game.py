class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:


        def calc_score(player1):
            p1 = 0
            for i, score in enumerate(player1):
                if (i > 0 and player1[i-1] == 10) or (i > 1 and player1[i-2] == 10):
                    p1 += 2* score
                else:
                    p1 += score
            return p1

        p1 = calc_score(player1)


        p2 = calc_score(player2)

        if p1 == p2:
            return 0

        elif p1 > p2:
            return 1

        else:
            return 2
