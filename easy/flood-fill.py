class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[1,0], [-1,0], [0, -1], [0,1]]
        n, m = len(image), len(image[0])
        
        def dfs(i, j, original):
            nonlocal color, n, m
            image[i][j] = color

            for down, right in directions:
                ti = i + down
                tj = j + right

                if 0 <= ti < n and 0 <= tj < m and image[ti][tj] == original and image[ti][tj] != color:
                    dfs(ti, tj, original)

        dfs(sr, sc, image[sr][sc])
        return image
