class Solution:
    def maximumLength(self, nums: List[int]) -> int:
    
        freq = {}

        for e in nums: 
            if e not in freq:
                freq[e] = 0
            freq[e] += 1

        _max = 0
        for e in set(nums):
            if e == 1:
                num_ones = freq[1]
                
                if num_ones % 2 == 0:
                    num_ones -= 1
                _max = max(_max, num_ones)
                continue
            
            curr_count = 0
            temp = e
            while temp in freq and freq[temp] > 0:
                if freq[temp] == 1:
                    curr_count += 1
                    last_was_one = True
                    break


                curr_count += 2
                temp = temp ** 2

            if curr_count % 2 == 0:
                curr_count -= 1

            _max = max(_max, curr_count) 
        return _max
            
        



