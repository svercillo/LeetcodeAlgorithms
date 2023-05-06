class Solution:
    def largestOverlap(self, img1, img2) -> int:
        n = len(img1)

        def overlap(rshift, dshift):
            nonlocal n
            total = 0

            for i in range(n):
                for j in range(n):
                    if 0 <= i + rshift < n and 0 <= j +  dshift < n:
                        if img1[i+rshift][j + dshift] == img2[i][j] == 1:
                            total += 1

            return total
        
        moverlap = 0
        for rshift in range(-n, n):
            for  dshift in range(-n, n):
                moverlap = max(
                    overlap(rshift, dshift),
                    moverlap
                )
        
        return moverlap
            
