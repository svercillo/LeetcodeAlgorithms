class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def pos_to_board(pos):
            n = len(board)
            pos -= 1

            row = 0
            while pos >= n:
                pos -= n 
                row += 1

            if row % 2 == 0: # left to right
                return board[n-1 - row][pos]
            else:
                return board[n-1 - row][n - 1 - pos]


        visited = set()
        q = [(1, False)]

        num_moves =0
        while len(q) > 0:
            new_q = []

            for pos, from_latter in q:
                if (pos, from_latter) in visited:
                    continue 
                
                visited.add((pos, from_latter))

                if pos == n**2: 
                    return num_moves

        
                for jumps in range(1, 7):
                    if pos + jumps <= n ** 2:
                        if pos + jumps not in visited:
                            if pos_to_board(pos+ jumps) != -1:
                                new_q.append((pos_to_board(pos + jumps), True))
                            else:
                                new_q.append((pos + jumps, False)) 

            q = new_q
            q.sort(reverse= True)
            num_moves += 1

        return -1
