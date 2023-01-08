class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [[set(), set(), set()], [set(), set(), set()]]
        cols = [[set(), set(), set()], [set(), set(), set()]]
        diag1 = [set(), set()]
        diag2 = [set(), set()]

        for turn, (i, j) in enumerate(moves):    
            if turn % 2 == 0:
                index = 0
            else:
                index = 1
            
            if index == 1:
                print(i, j)
            rows[index][i].add(j)
            cols[index][j].add(i)

            # print(rows[index])

            if len(cols[index][j]) == 3:
                return "A" if turn % 2 == 0 else "B"
            if len(rows[index][i]) == 3:
                return "A" if turn % 2 == 0 else "B"

            if i == j:
                diag1[index].add(i)
                if len(diag1[index]) == 3: return "A" if turn % 2 == 0 else "B"

            if j == -i + 2:
                diag2[index].add(j)
                if len(diag2[index]) == 3: return "A" if turn % 2 == 0 else "B"


        # A   B   A
        # B   B   B 
        # A   A  
        return "Draw" if len(moves) == 9 else "Pending"
