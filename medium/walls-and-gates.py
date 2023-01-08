class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms), len(rooms[0])


        q = [] 
        for i in range(n):
            for j in range(m):
                if rooms[i][j] ==0:
                    q.append((i,j))

        directions = [[0,-1], [-1, 0],[0,1],[1,0]]
        
        visited = set() 
        steps = 0
        while q:
            new_q = []

            for i, j in q:
                if (i,j) in visited:
                    continue

                visited.add((i,j))
                rooms[i][j] = steps

                for down, right in directions: 
                    ti, tj = i + down, j + right

                    if 0 <= ti < n and 0 <= tj < m and rooms[ti][tj] > 0:
                        new_q.append((ti,tj))

                        

            q = new_q
            steps += 1
