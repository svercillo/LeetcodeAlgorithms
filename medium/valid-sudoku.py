class Solution:
    def isValidSudoku(self, board) -> bool:

        unique_row = [set({}) for i in range(9)]
        unique_col = [set({}) for i in range(9)]

        for i in range(len(board)):

            for j in range(len(board[i])):

                if board[i][j] in unique_row[i] or board[i][j] in unique_col[j]:
                    return False

                elif board[i][j] != ".":
                    unique_row[i].add(board[i][j])
                    unique_col[j].add(board[i][j])
        for i in range(0, 9, 3):

            for j in range(0, 9, 3):

                digits = set({})
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] in digits:
                            print(digits)
                            return False
                        elif board[k][l] != ".":
                            digits.add(board[k][l])

        return True
