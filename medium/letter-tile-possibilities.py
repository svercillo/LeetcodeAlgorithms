class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
    
        n = len(tiles)
        words = set()
        
        count = 0
        freq = {}
        
        for c in tiles:
            if c not in freq:
                freq[c] = 0    
            freq[c] += 1
                    
                
        def dfs(string, freq:dict):
            if len(string) > 0:
                words.add(string)
            
            for c in freq:
                new_freq = freq.copy()
                new_freq[c] -= 1
                if new_freq[c] == 0:
                    new_freq.pop(c)
                
                new_string = "" + string + c
                dfs(new_string, new_freq)
                
        
        dfs("", freq)
        
        return len(words)
