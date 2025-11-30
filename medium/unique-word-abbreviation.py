from pprint import pprint
def abbr(word ):
    if len(word) < 3: 
        return word

    return word[0] + str(len(word) -2) + word[-1]

class ValidWordAbbr:

    def __init__(self, words: List[str]):
        self.mapping = defaultdict(set)
        for w in words:
            self.mapping[abbr(w)].add(w)
    
    def isUnique(self, word: str) -> bool:

        ab = abbr(word)

        if ab not in self.mapping: 
            return True

        return word in self.mapping[ab] and len(self.mapping[ab]) == 1




# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
