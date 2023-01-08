class Solution:
    count = 0
    def longestDecomposition(self, text: str) -> int:
        def recurse(text, start, end): # non-inclusive
            if start > end:
                return 

            o_start = start # original start
            o_end = end

            while start < end:

                if text[end] == text[o_start]:
                    if text[o_start:start+1] == text[end : o_end +1]:
                        print(text[o_start:start+1])
                        self.count +=2
                        recurse(text, start+1, end-1)
                        return 


                start +=1
                end -=1 


            self.count += 1
        
        
        recurse(text, 0, len(text)-1)
        
        return self.count
        
        
