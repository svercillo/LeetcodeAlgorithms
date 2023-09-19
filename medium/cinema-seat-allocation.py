class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        row_map = {}
        for row, col in reservedSeats:

            if row not in row_map:
                row_map[row] = set()

            row_map[row].add(col)

        print(row_map)
        
        count = 0
        for row in row_map: 
            selected = row_map[row]
            
            valid = True
            for e in [2, 3, 4, 5, 6,7,8,9]:
                if e in selected:
                    valid = False
                    break

            if valid:
                count += 2
                continue
            
            valid = True
            for e in [2, 3, 4, 5]:
                if e in selected:
                    valid = False
                    break

            if valid:
                count += 1
                continue



            valid = True
            for e in [4, 5 , 6, 7]:
                if e in selected:
                    valid = False
                    break
            if valid:
                count += 1
                continue


            valid = True
            for e in [6,7,8,9]:
                if e in selected:
                    valid = False
                    break
            if valid:
                count += 1
                continue

        return count +  (n -len(row_map)) * 2
