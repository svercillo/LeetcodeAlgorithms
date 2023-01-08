class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        start =0
        end = 1 # end is inclusive
        count = 1
        
        i = 0
        
        while end < len(chars):
            if chars[end] == chars[end -1]:
                count +=1
            else:

                chars[i] = chars[end-1] 
                i += 1
                
                if count != 1:
                    
                    for c in str(count):
                        chars[i] = c
                        i +=1 
                
                start = end
                count = 1
            
            end += 1
        
        
        chars[i] = chars[end-1] 
        i += 1
        
        if count != 1:

            for c in str(count):
                chars[i] = c
                i +=1 
                
        start = end
        count = 1
        
        return i
