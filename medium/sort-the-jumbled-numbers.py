class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def get_mapping_value(e):
            val = 0
            e_str = str(e)
            for i, c in enumerate(e_str):
                val += mapping[int(c)] * (10 ** (len(e_str) - i -1))
            return val
        
        zipped = zip(nums, [i for i in range(len(nums))])
        

        return [k[0] for k in sorted(zipped ,key=lambda k : (get_mapping_value(k[0]), k[1]))]

