class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])


        res = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append(".")
            res.append(row)


        print(n, m)
        stones = set()
        obstacles = set()
        for i in range(n):
            for j in range(m):
                element = box[i][j]
            
                if element == "*":
                    obstacles.add((j, n - i  -1))
                elif element == "#":
                    stones.add((j, n - i  -1))



        def find_lowest_location(i, j):
            nonlocal m
            while i + 1 < m and (i+1, j) not in obstacles and res[i+1][j] != "#":
                i += 1

            return i


        for i in range(m -1, -1, -1):
            for j in range(n):
                if (i, j) in stones:
                    lowest_i = find_lowest_location(i, j)

                    print(i,j)
                    if lowest_i != i:
                        res[i][j] = "."
                    res[lowest_i][j] = "#"

            
        for i, j in obstacles: 
            res[i][j] = "*"

        return res 

