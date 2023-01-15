class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        last = "-"
        for word in sentence.split():
            if last != "-":
                if word[0] != last:
                    return False

            last = word[-1]

        
        for c in sentence:
            if c != " ":
                return c == last
        
        return False