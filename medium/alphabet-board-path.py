class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        

        def get_char(i, j):
            return chr(5 * i + j + ord('a'))


        n = 5
        m = 5

        z_coords = (5, 0)

        dirs = [
            [[-1, 0], "U"],
            [[1, 0], "D"],
            [[0, 1], "R"],
            [[0, -1], "L"]
        ]

        q = [((0, 0), [], 0)]

        visited = set()
        
        while len(q):
            new_q = []

            for (i, j), path, string_ind in q:

                if ((i, j), string_ind) in visited:
                    continue



                if string_ind == len(target):
                    return "".join(path)
                 
                visited.add(((i, j), string_ind))

                character = get_char(i, j)

                # print(character, path, target[:string_ind])

                if character == target[string_ind]:
                    cpy = path.copy()
                    cpy.append("!")

                    new_q.append(((i, j), cpy, string_ind + 1)) 

                for (down, right), direction in dirs:
                    ti = i + down
                    tj = j + right

                    if (
                        (ti, tj) == z_coords 
                        or (
                            0 <= ti < n 
                            and 0 <= tj < m
                        )
                    ):
                        cpy = path.copy()
                        cpy.append(direction)
                        new_q.append(((ti, tj), cpy, string_ind))
                    

            q = new_q

        
        return []
