class Solution:
    def reverseWords(self, s: str) -> str:
        
        re.sub("[^\w\s]", " ", s)
        
        
        arr = s.split()
        # print(arr)
        
        
        res = arr[len(arr) -1]
        
        for i in range(len(arr)-2, -1, -1):
            if i <0: break
            res += " "
            res += arr[i]
            
        return res
