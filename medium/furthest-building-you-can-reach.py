class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # greedy

        ind = 0
        n = len(heights)

        
        already_added = False

        heap = []
        while ind < n-1:            
            # print(ind, bricks, ladders, heap)
            if heights[ind+ 1] > heights[ind]:
                needed = heights[ind+ 1] - heights[ind] 

                if not already_added:
                    heapq.heappush(heap, -needed)
                
                if bricks >= needed:
                    bricks -= needed
                    ind += 1
                    already_added = False
                else:
                    if ladders > 0:
                        ladders -= 1
                    else:
                        return ind # no more ladders, and saved as many bricks as possible, can't jump
                    most_saved = -heapq.heappop(heap)
                    bricks += most_saved
                    already_added = True
                    # don't iterate till next index
            else:
                ind += 1


        return ind
