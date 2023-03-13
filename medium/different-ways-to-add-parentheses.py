import math
class Solution:
    def diffWaysToCompute(self, expression: str):


        numbers = []
        operations = []
        num = ""
        for c in expression:

            if c in {'+', '-', '*'}:
                numbers.append(int(num))
                operations.append(c)
                num = ""
            else:
                num += c
    
        numbers.append(int(num))

        if len(numbers) == 1: 
            return [int(expression)]

        def collapse(left, right, op):

            match op:
                case '+':
                    return left + right
                case '-':
                    return left - right
                case '*':
                    return left * right

        visited = set()
        def recurse(nums, operations, results, num_ids):

            num_ids_tup = tuple(num_ids)
            if num_ids_tup in visited:
                return
            
            visited.add(num_ids_tup)
            # print(num_ids)
        
            if len(nums) == 2:
                processed_num = collapse(nums[0], nums[1], operations[0])
                results.append(processed_num)
                return
            
            for i in range(len(nums)-1): 
                
                processed_num = collapse(nums[i], nums[i+1], operations[i])
                
                new_nums = []
                new_operations = []
                new_num_ids = []
                for j in range(len(nums)):
                    if j == i:
                        continue 
                    elif j == i +1:
                        new_nums.append(processed_num)
                        new_num_ids.append("(" +  num_ids[j-1] +  "_" +  num_ids[j] + ")")
                        if j < len(operations): new_operations.append(operations[j])
                    else:
                        
                        new_num_ids.append(num_ids[j])
                        new_nums.append(nums[j])
                        if j < len(nums) -1: new_operations.append(operations[j])
                
                recurse(new_nums, new_operations, results, new_num_ids)
        

        num_ids = [str(num) for num in numbers]
        res = []
        recurse(numbers, operations, res, num_ids)

        return res
