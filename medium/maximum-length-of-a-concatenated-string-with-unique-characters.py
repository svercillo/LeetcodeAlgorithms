class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def validword(word):
            freq = defaultdict(int)
            for c in word:
                if freq[c] == 1: 
                    return False
                freq[c] += 1
            return True

        def cvalue(c):
            return ord(c) - 97

        def buildmask(wind):
            w = arr[wind]
            mask = 0
            for c in w:
                mask |= 1 << cvalue(c)
            return mask

        @cache
        def largest(ind, used_mask):
            if ind == n:
                return used_mask
            wmask = buildmask(ind)
            value0 = largest(ind + 1, used_mask)

            # is it possible to add word
            if wmask & used_mask == 0:
                
                value1 = largest(ind + 1, wmask | used_mask)

                if value1.bit_count() > value0.bit_count():
                    return value1
            return value0
                        
            
        
        arr = [word for word in arr if validword(word)]
        n = len(arr)
        return largest(0, 0).bit_count()
        


        
