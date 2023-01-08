from collections import deque
from pprint import pprint
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        subboxes = {}

        rows, cols = [], []
        for i in range(9):
            rows.append(set())
            cols.append(set())

        for i in range(3):
            for j in range(3):
                subboxes[(i, j)] = set()

        to_do = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    to_do.append((i,j))
                else:
                    board[i][j] = int(board[i][j])
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    subboxes[(i // 3, j // 3)].add(board[i][j])
            
        def dfs(index):
            nonlocal rows, cols, to_do
            if index == len(to_do):
                return True
            
            i, j = to_do[index]

            # print(i, j, (i // 3, j // 3))
            subbox = subboxes[(i // 3, j // 3)]
            for k in range(1,10):
                if k in rows[i]:
                    continue
                if k in cols[j]:
                    continue
                
                if k in subbox:
                    continue

                rows[i].add(k)
                cols[j].add(k)
                subbox.add(k)
                board[i][j] = k

                if dfs(index + 1): return True

                if k in rows[i]: rows[i].remove(k)
                if k in cols[j]: cols[j].remove(k)
                subbox.remove(k)
                board[i][j] = -1                
        dfs(0)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])

        pprint(board)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
res = Solution().solveSudoku(board)
