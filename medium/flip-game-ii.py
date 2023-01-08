class Solution:
    def canWin(self, currentState: str) -> bool:
        string = currentState

        swap = {"+": "-"}        
        
        def generateChoices(string):
            possible = list()
            n = len(string)
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
        
        possible_choices = generateChoices(string)
        
        
        def dfs(possible_choices, myturn):
            
            if len(possible_choices) == 0:
                return not myturn
            
            
            if not myturn:
                res = True
                for choice in possible_choices:
                    res = res and dfs(generateChoices(choice), not myturn)
                
                return res
            else:
                res = False
                for choice in possible_choices:
                    res = res or dfs(generateChoices(choice), not myturn)
                    
            
                return res
                
            
            
        return dfs(possible_choices, True)
