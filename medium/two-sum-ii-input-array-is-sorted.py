class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        
        
        freq = {}
        for i in range(len(numbers)):
            e = numbers[i]
            if e not in freq:
                freq[e] = [i]
                
            else: 
                freq[e].append(i)
        
        print(freq)
        i =0
        while i < n:
            e = numbers[i]
            
            diff = target - e
            if diff in freq:
                if diff == e:
                    return [freq[e][0] +1, freq[e][1]+1]
                else:
                    return [freq[e][0]+1, freq[diff][0]+1]
            i += 1
