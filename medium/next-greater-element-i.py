class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = set(nums1)
        inds = {}
        
        last_n = [] 
        for i, n in enumerate(nums2):
            for j in range(len(last_n) -1 , -1, -1):
                
                if n > last_n[j]:
                    inds[last_n[j]][1] = n
                    last_n.pop(j)
                
            if n in n1: 
                inds[n] = [i, -1]
                last_n.append(n)
        
        res = []
        for n in nums1:
            res.append(inds[n][1])
            
        
        return res
