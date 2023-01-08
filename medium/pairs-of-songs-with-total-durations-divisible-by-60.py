class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        n = len(time)
        
        freq_map = {}
        
        for i in range(n):
            value = time[i] %  60
            time[i] = value
            
            if value not in freq_map:
                freq_map[value] = 0
                
            freq_map[value] += 1
            
            
        print(freq_map)
        count = 0 
        
        for k in freq_map: 
            

            if 60 - k in freq_map:
                if 60 -k == k:
                    frq = freq_map[k]
                    
                    count += frq* (frq-1) /2

                else:
                    if 60 - k > k: continue
                    
                    
                    count += freq_map[k] * freq_map[60-k]

            elif k == 0:
                frq = freq_map[k]
                count += frq* (frq-1) /2

        return int(count)
