class Solution:
    def countVowelStrings(self, n: int) -> int:
        chars = ["a","e","i","o","u"]


        @lru_cache
        def num_strings(stringlen, last_char_ind, stoplen):
            if stringlen == stoplen:
                return 1
            
            num_strs = 0
            for ind in range(last_char_ind, len(chars)):
                num_strs += num_strings(stringlen +1, ind, stoplen)

            return num_strs

        
        total = 0
        for i, _ in enumerate(chars):
            total += num_strings(1,i, n)

        return total
