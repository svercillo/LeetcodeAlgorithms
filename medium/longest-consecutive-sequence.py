class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class Num:
            def __init__(self):
                self.val = 1
                
            def __repr__(self):
                # return str(id(self))
                return str(self.val)
        
        if len(nums) == 0 :
            return 0
        lengths = {}
        
        for n in nums:
            lengths[n] = [Num(), set([n])]
            
        
        max_val = 1
        for k in lengths:
            # print(k)
            if k +1 in lengths:
                # print(k, k+1, lengths[k])
               
                num1, added1 = lengths[k]
                num2, added2 = lengths[k+1]
                
                
                added1.add(k+1)
                total = num1.val + num2.val
                max_val = max(max_val, total)
                
                num1.val = total

                for added in added2:
                    added1.add(added)
                    lengths[added] = lengths[k]
            else: 
                # print(lengths[k])
                max_val = max(max_val, lengths[k][0].val)

                  
                
        # print([(id(lengths[n]), n) for n in lengths])
                
                
    
        return max_val
                        
            
            
            
            
