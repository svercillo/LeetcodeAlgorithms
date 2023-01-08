class Solution:
    def findLongestWord(self, s: str, arr: List[str]) -> str:
        m_str = ""
        for w in arr:
            if len(w) > len(s): continue
            
            start1 = 0
            start2 = 0
            
            valid = False
            while True:
                
                if start1 >= len(w) or start2 >= len(s): break
                
                
                if start1 == len(w) -1 and s[start2] == w[start1]:
                    valid = True
                    break
                
                
                if s[start2] == w[start1]:
                    start1 +=1
                    start2 +=1 
                else:
                    start2 +=1
                    
            if valid:
                if len(w) > len(m_str):
                    m_str = w
                elif len(w) == len(m_str) and w < m_str:
                    m_str = w
            
        return m_str
