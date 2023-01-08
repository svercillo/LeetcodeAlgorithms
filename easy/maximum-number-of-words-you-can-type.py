class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        broken = set([c for c in brokenLetters])
        valid_words = 0

        for word in text.split():
            print(word)
            valid_word = True
            for c in word:
                if c in broken:
                    valid_word = False
                    break

            if valid_word:
                valid_words += 1
        
        return valid_words
