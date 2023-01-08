class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        l = len(original)

        if l != m * n: 
            return []
        
        res = []
        curr = []
        for i in range(l):
            curr.append(original[i])
            if (i +1) % n == 0: 
                res.append(curr)
                curr = []
        return res
                
                
            
        
