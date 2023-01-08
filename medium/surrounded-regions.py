class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
    
        def flippable(i,j, visited) -> bool:
            nonlocal n, m

            

            if (i, j) in visited:
                return True

            print(i, j)

            visited.add((i, j))
            isflippable = True

            for down, right in dirs:
                ti = i + down
                tj = j + right

                if not (0 <= ti < n and 0 <= tj < m):
                    isflippable = False
            
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if 0 <= ti < n and 0 <= tj < m and board[ti][tj] == "O":
                    if not flippable(ti, tj, visited):
                        isflippable = False

            return isflippable


        to_remove = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    visited = set()
                    if (i, j) in to_remove:
                        continue 
                    if flippable(i, j, visited):
                        to_remove = to_remove.union(visited)

                        
        for i, j in to_remove:
            board[i][j] = "X"