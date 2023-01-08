class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        def process(s):
            n = len(s)

            start = 0
            end = 0
            chars  = {} 

            most_repeated = 0 
            mcount = 0 

            while end < n:
                if s[end] not in chars:
                    chars[s[end]] = 1
                else:
                    chars[s[end]] += 1
                
                most_repeated = max(most_repeated, chars[s[end]])

                if end -start + 1 - most_repeated > k:
                    chars[s[start]] -=1
                    start +=1 
                
                if end -start +1 > mcount:
                    mcount = end - start + 1 
                end += 1

            return mcount

        return process(s)
