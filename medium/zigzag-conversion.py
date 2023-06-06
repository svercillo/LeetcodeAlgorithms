class Solution:
    def convert(self, s: str, n_rows: int) -> str:
        
        ind = 0
        n = len(s)

        print(n)

        if n_rows == 1:
            return s

        elif n_rows == 2:
            carr = []
            for i in range(0, n, 2):
                carr.append(s[i])

            for i in range(1, n, 2):
                carr.append(s[i])

            return "".join(carr)

        grid = []


        width = 0
        ind = 0
        while ind < n:
            ind += n_rows
            ind += n_rows - 2
            width += 1 + n_rows - 2

            # print(ind, width)
            # break


        for i in range(n_rows):
            row = [" "] * (width * 2)

            grid.append(row)
            
        i =0
        j = 0
        ind = 0
        while ind < n:
            if i == 0:
                while i < n_rows and ind < n:
                    grid[i][j] = s[ind]
                    i += 1
                    ind += 1

                # move to bottom of next col
                j += 1 
                i = n_rows - 2
            else:
                grid[i][j] = s[ind]
                i -= 1
                j += 1
                ind += 1
        

        # from pprint import pprint
        # for row in grid:
        #     print(row)

        carr = []
        for i in range(len(grid)):

            row = []
            for j in range(len(grid[0])):
                if grid[i][j] == " ":
                    continue
                

                row.append(grid[i][j])
                carr.append(grid[i][j])

            # print(row)

        return "".join(carr)
