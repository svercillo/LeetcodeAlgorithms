class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        
        freq = {}
        for c in s: 
            if c not in freq:
                freq[c] = 0
                
            freq[c] += 1
        
        
        inputs = sorted([(a, freq[a]) for a in freq], key = lambda k : k[1], reverse=True)
        
        total = 0
        presses = 1
        number = 0
        for c, freq in inputs:
            if number == 9:
                presses += 1
            number = number % 9
            number += 1
            
            
            total += presses * freq
            
            
        
        return total
            
