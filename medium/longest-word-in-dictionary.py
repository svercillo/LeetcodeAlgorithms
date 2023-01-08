from collections import Counter
class Solution:
    def longestWord(self, words) -> str:
        n = len(words)
        words.sort()
        s = set(words)

        m_str = ""
        curr_str = ""
        
        fc  = None # first char 
        for i in range(n):
            if fc is None or fc != words[i][0]:
                # print(curr_str)
                if len(words[i])==1: 
                    fc = words[i]
                    curr_str = fc
                else: 
                    fc = None
            else: 
                # print(curr_str)
                # check ith w can be built from previous
                if words[i][:len(words[i])-1] == curr_str:
                    curr_str = words[i]
                    
                    
                    
                else: 
                    if words[i][0] == fc: 
                        invalid = False
                        for k in range(len(words[i])-1):
                            print(words[i][:k +1])
                            if words[i][:k +1] not in s:
                                invalid = True
                                break
                        
                        if not invalid:
                            curr_str = words[i]
    
                            
                if len(curr_str) > len(m_str):
                        m_str = curr_str

        
        return m_str
                    
