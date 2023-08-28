class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = []
        for w in words: 
            if not len(w):
                return False


            res.append(w[0])

        return "".join(res) == s
