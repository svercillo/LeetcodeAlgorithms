class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        '''
        idea:
            store the running OR of all elements 
            for each bit in the OR store the latest index that the bit was set at
            iterate through all the possible latest indexes in order from greatest to least
            add to set if not in             
        '''

        res = set()
        added_last = set()
        for num in arr:
            next_added_last = set()

            for numj in added_last:
                next_added_last.add(num | numj)
                res.add(num | numj)
            next_added_last.add(num)
            res.add(num)

            added_last = next_added_last

        return len(res)
