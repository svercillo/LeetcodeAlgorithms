from pprint import pprint
import math

class Solution:
    def minimumOperations(self, nums) -> int:

        if len(nums) == 1:
            return 0

        n = len(nums)
        odd_freq = {}
        even_freq = {}
        even = True
        for e in nums:

            if even:
                if e not in even_freq:
                    even_freq[e] = 0
                even_freq[e] += 1
            else:
                if e not in odd_freq:
                    odd_freq[e] = 0
                odd_freq[e] += 1

            even = not even
        
        def highest_two_freqs(freq_map):

            largest = None
            sec_largest = None
            for k in freq_map:
                if largest is None:
                    largest = k
                elif freq_map[k] > freq_map[largest]:
                    sec_largest = largest
                    largest = k
                elif sec_largest is None:
                    sec_largest = k
                elif freq_map[k] > freq_map[sec_largest]: 
                    sec_largest = k

                print(k, largest, sec_largest)

            return (largest, sec_largest)

            
        e1, e2 = highest_two_freqs(even_freq)
        o1, o2 = highest_two_freqs(odd_freq)

        res = math.inf

        if o1 == e1:
            if o2 is not None:
                res = min(res, n - even_freq[e1] - odd_freq[o2])

            if e2 is not None:
                res = min(res, n - even_freq[e2] - odd_freq[o1])

            res = min(res, n - even_freq[e1], n - odd_freq[o1])
        else:
            res = min(res, n - even_freq[e1] - odd_freq[o1])

        return res
