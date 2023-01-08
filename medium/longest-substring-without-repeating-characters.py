class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding door
        if not s:
            return 0
        if len(s) ==2 and s[0] != s[1]:
            return 2
        
        i = 0
        j = 1
        m = set({s[0]})
        m_map = {}
        m_len = 1
        while i < len(s)-1:

            if len(m) > m_len:

                m_len = len(m)
                m_map = m.copy()
            
            if s[j] not in m:

                m.add(s[j])
                if len(m) > m_len:
                    m_len = len(m)
                    m_map = m.copy()
                if j != len(s) -1:
                    j += 1
                else: 
                    i +=1
            else:
                m.remove(s[i])
                i +=1
        
        
        if j-i > m_len:
            m_len = j - i + 1
            m_map = m.copy()
        return m_len
