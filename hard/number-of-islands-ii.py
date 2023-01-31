class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # union-find

        graph = {} # maps coords to root_coords
        sizes = {} # maps root coords to size of island


        dirs = [[0,1], [0,-1], [1, 0,], [-1, 0]]


        def find_root_coords(i,j):
            while graph[(i,j)] != (i,j):
                i, j = graph[(i, j)]

            return i, j

        def union(root_coords_arr):
            biggest_island_root_coords = None
            largest_island_size = -1
            total_size = 0
            for root_coords in root_coords_arr: 
                size = sizes[root_coords]
                total_size += size
                if size > largest_island_size:
                    largest_island_size = size
                    biggest_island_root_coords = root_coords

            for root_coords in root_coords_arr:
                graph[root_coords] = biggest_island_root_coords
            sizes[biggest_island_root_coords] = total_size


        res = []
        num_islands = 0

        visited = set()
        for i, j in positions:

            if (i, j) in visited:
                res.append(num_islands)
                continue
            visited.add((i,j))


            root_coords_arr = set() 
            graph[(i, j)] = (i, j)
            sizes[(i,j)] = 1
            root_coords_arr.add((i,j))
        

            for down, right in dirs: 
                ti = i + down
                tj = j + right

                if 0<= ti < m and 0<= tj < n: 
                    if (ti, tj) in graph:
                        root_coords_arr.add(find_root_coords(ti, tj))

            union(root_coords_arr)

            num_islands += 2 - len(root_coords_arr)


            res.append(num_islands)


        return res

