class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        l, r = 0, 0 
        n = len(word)

        freq = {}

        limits = {"a" : 0, 'e' : 1, 'i': 2, 'o' : 3, 'u': 4}
        longest = 0
        while r < n:

            letter = word[r]
            
            if l != -1 and len(freq) == limits[letter] + (1 if letter in freq else 0):
                if letter not in freq:
                    freq[letter] = 0
                freq[letter] += 1
            else:
                freq = {}
                if letter == 'a':
                    freq = {'a' : 1}
                    l = r
                else:
                    l = -1


            if l != -1 and len(freq) == 5:
                longest = max(longest, r-l + 1)

            r += 1



        return longest
