class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        
        n = len(s)
        start, stop = 0, k-1 # inclusive
        
        _max = 0
        for i in range(k):
            if s[i] in vowels:
                _max += 1


        num_v = _max
        
        start += 1
        stop += 1
        
        while stop != n:

            if s[start-1] in vowels:
                num_v -=1
            
            if s[stop] in vowels: 
                num_v += 1
            
            _max = max(_max, num_v)
            
            start += 1
            stop += 1
            
        return _max
            
