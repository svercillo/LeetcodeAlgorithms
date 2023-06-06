class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for word in words:

            even = []
            odd = []
            i = 0
            while i < len(word):
                even.append(word[i])

                if i + 1 < len(word):
                    odd.append(word[i+1])

                i += 2

            even.sort()
            odd.sort()

            groups.add(tuple([tuple(even), tuple(odd)]))


        return len(groups)
