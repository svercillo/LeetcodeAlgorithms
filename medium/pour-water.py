Select tags
0/5
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        # idea: dfs each time?
        
        def will_move_left(index):
            if index == 0: return index

            for i in range(index, -1, -1):
                if heights[i] < heights[index]:
                    return will_move_left(i)

                elif heights[i] > heights[index]:
                    return index


            return index
                    
        def will_move_right(index):
            if index == len(heights)-1: return index
            
            for i in range(index, len(heights)):
                if heights[i] < heights[index]:
                    return will_move_right(i)
                
                elif heights[i] > heights[index]:
                    return index
                
            return index

        while volume:
            lind = will_move_left(k)
            rind = will_move_right(k)

            print(lind, rind)

            if lind != k:
                heights[lind] += 1
            
            elif rind != k:
                heights[rind] += 1
            else:
                heights[k] += 1            
            volume -= 1


        return heights
