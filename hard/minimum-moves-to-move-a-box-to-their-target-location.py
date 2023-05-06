class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        person = None
        box = None
        target = None

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "S":
                    person = (i, j)
                    grid[i][j] = "."
                elif grid[i][j] == "B":
                    box = (i, j)
                    grid[i][j] = "."
                elif grid[i][j] == "T":
                    target = (i, j)
                    grid[i][j] = "."
        
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        
        visited = {}
        q = [(person, box, 0)]

        min_num_pushes = math.inf

        while len(q):
            new_q = []

            for person, box, num_pushes in q:
                if (person, box) in visited and num_pushes >= visited[(person, box)]:
                    continue

                # print(person, box)
                visited[(person, box)] = num_pushes

                # print(box, target)
                if box == target:
                    min_num_pushes = min(
                        num_pushes,
                        min_num_pushes
                    )
                    continue

                for down, right in dirs:
                    ti = person[0] + down
                    tj = person[1] + right

                    if 0 <= ti < n and 0 <= tj < m:
                        # print(ti, tj, 0 <= ti < n and 0 <= tj < m, (ti, tj) == box, grid[ti][tj])
                        if grid[ti][tj] == "#":
                            continue
                        elif (ti, tj) == box: # trying to push box
                            ti2 = ti + down
                            tj2 = tj + right

                            if 0 <= ti2 < n and 0 <= tj2 < m:
                                if grid[ti2][tj2] == ".":
                                    # print("pushing")
                                    new_q.append(
                                        (
                                            (ti, tj), # new player pos
                                            (ti2, tj2),
                                            num_pushes + 1
                                        ) # new box pos
                                    )
                        else:
                            # print(ti, tj)
                            # print("not pushing")
                            new_q.append(
                                (
                                    (ti, tj), # new player pos 
                                    box, # box doesn't move
                                    num_pushes
                                )
                            )
            q = new_q


        if min_num_pushes == math.inf:
            return -1

        return min_num_pushes
                
