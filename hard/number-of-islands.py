class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])

        new_grid = []
        for i in range(n):
            row = [] 
            for j in range(m):
                row.append(grid[i][j])
            new_grid.append(row)
        
        grid = new_grid

        all_keys = []
        
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
        lockpos = {} # {lock, coords} 
        kcount = 0
        starting = (-1, -1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    starting = (i, j)
                elif grid[i][j].isalpha() and grid[i][j].isupper():
                    lockpos[grid[i][j]] = (i, j)
                    all_keys.append(grid[i][j].lower())
        
        all_keys.sort()
        all_keys = tuple(all_keys)      
          
                         
        def islock(i, j):
            return grid[i][j].isalpha() and grid[i][j].isupper()

        def iskey(i, j):
            return grid[i][j].isalpha() and grid[i][j].islower()

        def get_ordered_keys(key_coords):
            return tuple(sorted([key_coords[coords] for coords in key_coords]))


        
        nummoves = 0
        visited = set()
        q = [(starting[0], starting[1], {})]
        while len(q): 
            new_q = []
            for i, j, key_coords in q:
                keys_collected = get_ordered_keys(key_coords)

                if (i, j, keys_collected) in visited: 
                    continue
                visited.add((i,j, keys_collected))

                key_coords = key_coords.copy()

                if iskey(i,j) and (i,j) not in key_coords:
                    key_coords[(i,j)] = grid[i][j]
                    
                    keys_collected = get_ordered_keys(key_coords)
                    if keys_collected == all_keys:
                        return nummoves


                for down, right in directions:
                    ti, tj = i + down, j + right
                    if (
                        0 <= ti < n 
                        and 0 <= tj < m 
                        and (not islock(i,j) or grid[i][j].lower() in [key_coords[a] for a in key_coords])  
                        and grid[ti][tj] != "#"
                    ):
                        new_q.append((ti, tj, key_coords))

            nummoves += 1

            q = new_q

        return -1
