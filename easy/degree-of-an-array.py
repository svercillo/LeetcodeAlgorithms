import math
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        _map = {}
        
        for i, c in enumerate(nums):
            if c not in _map:
                _map[c] = [] 
                
            _map[c].append(i)
        
        m_len = -1 
        m_m_len = math.inf
        for k in _map:
            if len(_map[k]) >= m_len:
                if len(_map[k]) > m_len:
                    m_m_len = math.inf

                m_len = len(_map[k])
                print(m_len)
                
                if _map[k][-1] - _map[k][0] < m_m_len: 
                    print(k, _map)
                    m_m_len = _map[k][-1] - _map[k][0]
                    
                    
        return m_m_len + 1 
