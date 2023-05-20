class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False


        freq1, freq2 = {}, {}

        for c in word1: 
            if c not in freq1:
                freq1[c] = 0

            freq1[c] += 1

        for c in word2:
            if c not in freq2:
                freq2[c] = 0
            freq2[c] += 1

        
        chars1, chars2 = [], []
        freq_vals1, freq_vals2 = [], []

        for c in freq1:
            freq_vals1.append(freq1[c])
            chars1.append(c)

        for c in freq2:
            freq_vals2.append(freq2[c])
            chars2.append(c)

        chars1.sort()
        chars2.sort()
        freq_vals1.sort()
        freq_vals2.sort()

        if freq_vals1 == freq_vals2 and chars1 == chars2:
            return True

        else:
            return False
