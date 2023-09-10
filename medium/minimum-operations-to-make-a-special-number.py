class Solution:
    def minimumOperations(self, num: str) -> int:

        n = len(num )
        end_values = ['25', '50', '75', '00']


        def numDelete(end_value):
            end_ind = len(end_value) -1
            for i in range(n-1, -1, -1):

                if num[i] == end_value[end_ind]:
                    end_ind -= 1
                if end_ind == -1:
                    return n -1 - i -1 
                    
            return len(num)
        
        possible = []
        for end_value in end_values: 
            possible.append(numDelete(end_value))
            

        if "0" in num:
            possible.append(n-1)

        
        return min(possible)
