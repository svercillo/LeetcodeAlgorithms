class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        string = currentState
        swap = {"+": "-"}
        
        # if n <= 2: 
        #     return []
        
        possible = list()
        
        for i in range(n -1):            
            c = string[i]
            
            if string[i +1] == string[i] == "+":
                possible.append(i)
        
        result = []
        for index in possible:
            arr = list(string)
            
            arr[index] = swap[arr[index]]
            arr[index +1] = swap[arr[index+1]]
            
            result.append("".join(arr))
    
        return result
            
            
            


            
                
                
                
            
