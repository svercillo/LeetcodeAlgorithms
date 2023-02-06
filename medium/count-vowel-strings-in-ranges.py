class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o','u']
        
        
        prefix = 0
        presum = []
        for ind, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix += 1
            presum.append(prefix)
            

        res = []
            
        for l, r in queries:

            diff = presum[r] 
            
            if l - 1 >= 0:
                diff -= presum[l -1]
                
            
            res.append(diff)


        return res
        
        
                
                
        
        
