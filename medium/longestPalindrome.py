class Solution:
    def longestPalindrome(self, s: str) -> str:        
        n = len(s)
        i =0
        j = 1
        
        m_len = 0
        m_str = ""
        
        start = True
        for i in range(n):
            upper = i +1
            lower = i -1 
            
            print(i, upper, lower)
            _len = 1
            while upper < n and lower >= 0 and s[upper] == s[lower]:
                _len  += 1
                upper += 1
                lower -= 1
                
            if _len > m_len:
                m_len =_len
                m_str = s[lower +1: upper]
                print(m_str)
                
        
        for i in range(n):   
            upper1 = i+1
            lower1 = i
            
            _len1 = 1
            while upper1 < n and lower1 >= 0 and s[upper1] == s[lower1]:
                _len1  += 1
                upper1 += 1
                lower1 -= 1
                
            if _len1 > m_len:
                m_len =_len1
                m_str = s[lower1 +1: upper1]
                
            
        for i in range(n):
            upper2 = i
            lower2 = i-1
            
            _len2 = 1
            while upper2 < n and lower2 >= 0 and s[upper2] == s[lower2]:
                _len2  += 1
                upper2 += 1
                lower2 -= 1
                
            if _len2 > m_len:
                m_len =_len2
                m_str = s[lower2 +1: upper2]


            
            
        return m_str
            
