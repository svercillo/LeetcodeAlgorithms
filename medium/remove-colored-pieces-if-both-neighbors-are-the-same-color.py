class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        n = len(colors)
        movesA = 0
        movesB = 0

        for i, c in enumerate(colors):
            if 1 <= i <= n-2:
                if colors[i-1] == colors[i] == colors[i+1]:
                    if c == "A":
                        movesA += 1
                    else:
                        movesB += 1

        return movesA > movesB 
