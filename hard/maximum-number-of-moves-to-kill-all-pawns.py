class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        pawns = positions
        print(pawns)

        dirs = [
            [2, 1],
            [2, -1],
            [-2, 1],
            [-2, -1],
            [1, 2],
            [1, -2],
            [-1, 2],
            [-1, -2]
        ]

        n, m = 50, 50 


        @cache
        def optimalNumberofMoves(origin, target):
            # print("here" , origin, target)
            num_moves = 0
            q = [origin]

            visited = set()
            while len(q):
                new_q = []
                for i, j in q:

                    if (i,j) in visited:
                        continue
                    
                    visited.add((i,j))

                    if i == target[0] and j == target[1]:
                        # print("fsdfsdf", num_moves)
                        return num_moves 
   
                    for down, right in dirs:
                        ti = i + down
                        tj = j + right

                        if not (0 <= ti < n) or not (0 <= tj < m):
                            continue
                        
                        new_q.append((ti,tj))

                num_moves += 1
                q = new_q
            
            return -1


        @cache
        def countMovesRequired(aliceTurn:bool, bitmask, i, j):

            # print(bitmask, bin(bitmask ))
            if bitmask == 0:
                return 0

            min_moves = math.inf
            max_moves = 0
            
            for pawn_ind in range(len(pawns)):
                if not bitmask & (2 ** pawn_ind):
                    continue # pawn already down

                new_bit_mask = bitmask - 2 ** pawn_ind # after removing pawn
                pawn = pawns[pawn_ind]

                num_moves_to_remove = optimalNumberofMoves((i, j), tuple(pawn))

                res = countMovesRequired(not aliceTurn, new_bit_mask, pawn[0], pawn[1]) + num_moves_to_remove
                if res < min_moves: 
                    min_moves = res

                if res > max_moves:
                    max_moves = res

            if aliceTurn:
                return max_moves
            else:
                return min_moves

        return countMovesRequired(True, 2**len(pawns)-1, kx, ky) 
        



