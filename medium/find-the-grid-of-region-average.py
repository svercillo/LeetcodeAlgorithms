class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        n, m = len(image), len(image[0])

        dirs = [[0, 1], [1, 0]]


        regions = {} 

        for start_row in range(n-2):
            for start_col in range(m -2):
                invalidRegion = False
                _sum = 0

                # print(start_row, start_col)
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):

                        _sum += image[i][j]

                        # print((i,j))
                        for down, right in dirs: 
                            ti = i + down
                            tj = j + right
                            
                            if not (ti < start_row + 3 and tj < start_col + 3): 
                                continue
                            
                            diff = abs(image[i][j] - image[ti][tj])


                            if diff > threshold:
                                invalidRegion = True 
                                break
                        

                if invalidRegion:
                    continue

                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if (i,j) not in regions: 
                            regions[(i, j)] = []
                        regions[(i,j)].append(_sum  // 9)


        res = []
        for i in range(n): 
            row = []
            for j in range(m):
                if (i,j) not in regions:
                    row.append(image[i][j])
                else:
                    row.append(sum(regions[(i,j)]) // len(regions[(i,j)]))
            res.append(row)

        return res

