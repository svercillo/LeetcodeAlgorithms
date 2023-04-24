class Solution:
    def exist(self, board, word: str) -> bool:

        self.n = len(board)
        self.m = len(board[0])

        self.board = board

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = set({})
                    success = self.str_search(i, j, word, 0, visited)
                    if success:
                        return True

        return False

    def str_search(self, i, j, string, str_ind, visited):  # dfs

        if str_ind >= len(string):
            return True  # yayyyy

        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            return False

        # if self.visited[i][j] == 0 and self.board[i][j] == string[str_ind]:
        if (i, j) not in visited and self.board[i][j] == string[str_ind]:
            # print(self.board[i][j], i, j, string[str_ind])
            str_ind += 1

            visited.add((i, j))
            res = (
                self.str_search(i + 1, j, string, str_ind, visited)
                or self.str_search(i - 1, j, string, str_ind, visited)
                or self.str_search(i, j + 1, string, str_ind, visited)
                or self.str_search(i, j - 1, string, str_ind, visited)
            )
            visited.remove((i, j))

            return res
        else:
            # print((i, j), visited)
            return False
