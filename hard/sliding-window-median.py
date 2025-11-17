
from heapq import heappush, heappop
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]: 
        '''
        idea:
            max heap the left side of the window
            min heap the right side of the window
            when sliding window make index invalid
                keep invalid indexes set
            add new element to one side
            rebalance the heaps
                keep count of invalid on one side and the other in mind            
        '''


        smallest = min(nums) + 1
        nums = [e + abs(smallest) for e in nums] 

        def trim(left, right):
            nonlocal ltombs, rtombs
            while len(left) and left[0][1] in tombstones:
                heappop(left)
                ltombs -= 1

            while len(right) and right[0][1] in tombstones:
                heappop(right)
                rtombs -= 1

        def balance(left,right, tombstones):
            nonlocal ltombs, rtombs 

            trim(left, right)
            sizel = len(left) - ltombs
            sizer = len(right) - rtombs

            

            assert sizel + sizer == k        
            while  (
                not (sizel == ceil(k / 2) and sizer == k // 2)
            ):
                trim(left, right)
                sizel = len(left) - ltombs
                sizer = len(right) - rtombs

                if sizel < ceil(k / 2): # move from right to left
                    val, ind = heappop(rheap)
                    
                    if ind in tombstones: 
                        # element no longer in the window: skip!
                        rtombs -=1
                    else:
                        heappush(lheap, (-val, ind))
                else:
                    val, ind = heappop(lheap)
                    val *= -1

                    if ind in tombstones: 
                        # element no longer in the window: skip!
                        ltombs -=1

                    heappush(rheap, (val, ind))
                
                trim(left, right)
                sizel = len(left) - ltombs
                sizer = len(right) - rtombs

            

        def getMedian(left, right, tombstones):
            nonlocal ltombs, rtombs
            sizel = len(left) - ltombs
            sizer = len(right) - rtombs

            assert (sizel == ceil(k / 2) and sizer == k // 2)

            if k % 2 ==1:
                return -lheap[0][0]
            
            # print(lheap, rheap)
            return (-lheap[0][0] + rheap[0][0]) / 2
        
        def remove(ind): 
            nonlocal ltombs, rtombs
            lval = nums[ind] 
            if len(lheap) and lheap[0][1] == ind:
                heappop(lheap)
                return
            if len(rheap) and rheap[0][1] == ind:
                heappop(rheap)
                return 
            if lval <= -lheap[0][0]: # if removed element was on lhs
                ltombs += 1
            else:
                rtombs += 1            
            tombstones.add(l)
            
        n = len(nums)
        lheap, rheap = [], []
        for i, e in enumerate(nums[:k-1]):
            heappush(rheap, (e, i))

        res = []
        ltombs, rtombs = 0,0
        tombstones = set()
        l = 0
        r = k-1
        while r < n:
            rval  = nums[r] 

            if len(lheap): 
                if rval <= -lheap[0][0]: 
                    heappush(lheap, (-rval, r))
                else:
                    heappush(rheap, (rval, r))
            else:
                if len(rheap) and rval <= rheap[0][0]: 
                    heappush(lheap, (-rval, r))
                else:
                    heappush(rheap, (rval, r))
            # print("before" , lheap, rheap, (ltombs, rtombs),tombstones )
            balance(lheap, rheap, tombstones)
            # print("after" , lheap, rheap, tombstones)
            median = getMedian(lheap, rheap, tombstones)
            # # print(nums[l:r+1], lheap, rheap, tombstones)
            
            res.append(median)

            remove(l)

            r += 1
            l += 1

        return [e - abs(smallest) for e in res]
