import math
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        num_flowers = n 
        flower = flowerbed
        n = len(flower)
        
        i = 0
        
        num = 0
        while i < n: 
            if flower[i] ==1: 
                i +=1 
                continue
            
            j = i

            while j < n and flower[j] == 0: 
                j +=1
            if i != 0: 
                start = i +1
            else: 
                start = i
                    
            if j != n: 
                end =j -1
            else: 
                end = j
                

            num += math.ceil((end - start) /2 )    
            i = j
        return num_flowers <= num
        
