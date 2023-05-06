class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])


        dirs = [
            [0, 1],
            [1, 0]
        ]
        def find_bottom_corner(i, j):
            nonlocal n, m
            visited.add((i, j))
            

            for down, right in dirs:
                ti = i + down
                tj = j + right

                if 0 <= ti < n and 0 <= tj < m and land[ti][tj] == 1:
                    return find_bottom_corner(ti, tj)

            return (i, j)

        res = []
        visited = set()
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and (i, j) not in visited:

                    
                    if i-1 >= 0 and land[i-1][j] == 1:
                        continue

                    bottomi, bottomj = find_bottom_corner(i, j)
                    res.append((i,j, bottomi, bottomj))

                    

        return res
