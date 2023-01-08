class Solution:
    def intervalIntersection(self, firstList, secondList):
        p1 = 0
        p2 = 0
        
        
        res = [] 
        
        i =0 
        while p1 < len(firstList) and p2 < len(secondList): 
            
            if (
                firstList[p1][0] > secondList[p2][0] 
                or (firstList[p1][0] == secondList[p2][0] and firstList[p1][1] > secondList[p2][1])
            ): # make sure first always starts
                temp = firstList
                tempp = p1 
                firstList = secondList
                secondList = temp
                p1 = p2
                p2 = tempp
            
            print(firstList[p1])
            # print(firstList[p1], secondList[p2])
            if firstList[p1][1] >= secondList[p2][0]:
                res.append( [secondList[p2][0], min(firstList[p1][1], secondList[p2][1])] )
                print("SDFSDF")
                if secondList[p2][1] < firstList[p1][1]:
                    # print("here", p1 < len(firstList) and p2 < len(secondList))
                    p2 +=1
                    
                    continue
            
            p1 += 1 

            
        return res
