class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda k : k[1], reverse= True)
        n = len(boxTypes)

        print(boxTypes)
        res = 0
        ind = 0
        while truckSize > 0 and ind < n:
            boxes_added = min(truckSize, boxTypes[ind][0])
            print(boxTypes[ind][1], boxes_added, boxes_added * boxTypes[ind][1])
            res += boxes_added * boxTypes[ind][1]
            
            truckSize -= boxes_added        
            ind += 1

        return res
