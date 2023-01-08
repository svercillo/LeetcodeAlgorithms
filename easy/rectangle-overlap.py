class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        rec1.extend(rec2)
        
        
        return self.computeArea(*rec1) != 0
        
        
        
        
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1 <= bx1:
            swap = False
        else:
            swap = True

        if swap:
            tx1, tx2, ty1, ty2 = ax1, ax2, ay1, ay2
            ax1, ax2, ay1, ay2 = bx1, bx2, by1, by2
            bx1, bx2, by1, by2 = tx1, tx2, ty1, ty2

        startx, stopx  = max(ax1, bx1),min(ax2, bx2)
        starty,stopy = max(ay1, by1), min(ay2, by2)

        # print( startx, stopx, starty,stopy )

        if stopx > startx and stopy > starty:
            shared = (stopx - startx) * (stopy - starty)
        else:
            shared = 0
        return shared
