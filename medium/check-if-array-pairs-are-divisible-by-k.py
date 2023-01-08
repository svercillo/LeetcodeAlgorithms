class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        freq = {}
        for e in arr: 
            if e % k not in freq:
                freq[e % k] = 0
            freq[e % k] += 1

        print(freq)
        for e in freq:

            if e == 0:
                if freq[e] % 2 != 0: 
                    return False
                
                continue
                
            if k - e not in freq:
                return False

            if freq[k - e] != freq[e]:
                return False
            

        return True