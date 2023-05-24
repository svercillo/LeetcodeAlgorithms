class Solution:
    def minDeletions(self, s: str) -> int:

        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0
            
            freq[c] += 1
    
        
        freq_map = {}

        for c in freq:
            if freq[c] not in freq_map:
                freq_map[freq[c]] = 0
            freq_map[freq[c]] += 1

        print(freq_map)
        count = 0

        keys = [f for f in freq_map]


        while len(keys):
            # print("before", freq_map, count)
            new_keys = []
            for f in keys:
                if freq_map[f] <= 1:
                    continue
                
                fnew = f
                while freq_map[fnew] > 1:
                    print(freq_map, freq_map[fnew])

                    prev = freq_map[fnew]
                    freq_map[fnew] = 1
                    count += prev - 1

                    if fnew == 1:
                        continue
                    if fnew - 1 not in freq_map:
                        freq_map[fnew -1] = 0
                    freq_map[fnew -1] += prev - 1
                    
                    fnew -= 1

                new_keys.append(fnew)
    
            # print("after", freq_map)
            keys = new_keys

        return count
