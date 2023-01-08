class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]

        def valid_square(tlc, blc, trc, brc) -> bool:
            # 1. parallel lines share the same slope
            vert_slope1 = (tlc[1] - blc[1]) / (tlc[0] - blc[0] if tlc[0] - blc[0] != 0 else math.inf) 
            vert_slope2 = (trc[1] - brc[1]) / (trc[0] - brc[0] if trc[0] - brc[0] != 0 else math.inf)

            if vert_slope1 != vert_slope2: return False

            horz_slope1 = (tlc[0] - trc[0]) / (tlc[1] - trc[1] if tlc[1] - trc[1] != 0 else math.inf) 
            horz_slope2 = (blc[0] - brc[0]) / (blc[1] - brc[1] if blc[1] - brc[1] != 0 else math.inf) 

            if horz_slope1 != horz_slope2: return False

            # 2. all lengths are the same
            len_top_line = ((tlc[0] - trc[0]) ** 2 + (tlc[1] - trc[1]) ** 2) ** 0.5 # pythagoroas
            len_bottom_line = ((blc[0] - brc[0]) ** 2 + (blc[1] - brc[1]) ** 2) ** 0.5 # pythagoroas

            if len_top_line != len_bottom_line: return False

            len_left_line = ((tlc[0] - blc[0]) ** 2 + (tlc[1] - blc[1]) ** 2) ** 0.5 # pythagoroas
            len_right_line = ((trc[0] - brc[0]) ** 2 + (trc[1] - brc[1]) ** 2) ** 0.5 # pythagoroas

            if not(len_bottom_line == len_left_line == len_right_line == len_top_line): return False

            diag1 = ((blc[0] - trc[0]) ** 2 + (blc[1] - trc[1]) ** 2) ** 0.5 # pythagoroas
            diag2 = ((tlc[0] - brc[0]) ** 2 + (tlc[1] - brc[1]) ** 2) ** 0.5 # pythagoroas

            if diag1 != diag2: return False
            return True
            

        point_set = set({*points})

        if len(point_set) != 4:
            return False
        for i in range(4): 
            for j in range(4):
                if i == j: continue
                
                tlc = points[i]
                blc = points[j]
                options = [t for t in range(4) if t not in [i, j]]

                for option in range(2):
                    if option == 0: 
                        trc = points[options[0]]
                        brc = points[options[1]]
                    else:
                        brc = points[options[0]]
                        trc = points[options[1]]
                    
                    if valid_square(tlc, blc, trc, brc): return True

        return False
