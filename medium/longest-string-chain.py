class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        smallest_l = math.inf
        map = {}
        for w in words: 
            l = len(w)
            if l not in map:
                map[l] = set()
            map[l].add(w)

            smallest_l = min(l, smallest_l)
        

        @cache
        def longestChain(word): 
            l = len(word)
            if l not in map or word not in map[l]:
                return 0

            longest = 0
            for i in range(26):
                c = chr(97 + i)

                for j in range(l+1): 
                    # print(word, word[:j] + c + word[j:])
                    val = longestChain(word[:j] + c + word[j:]) + 1
                    
                    if val > longest:
                        longest = val

            return longest

        longest = 0
        for w in words:
            longest = max(longest, longestChain(w))

        return longest


            








        

        

            
      
