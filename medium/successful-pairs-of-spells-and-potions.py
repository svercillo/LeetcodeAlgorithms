class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        res = []
        for spell in spells:
            required_potion = math.ceil(success / spell)

            ind = bisect.bisect_left(potions, required_potion)

            if ind == len(potions):
                res.append(0)
                continue

            count = len(potions) - ind
            res.append(count)
            print(spell, required_potion, ind, potions[ind])

        return res
