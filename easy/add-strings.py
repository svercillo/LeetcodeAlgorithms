class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            t = num1
            num1 = num2
            num2 = t
        carr1 = [c for c in num1[::-1]]
        carr2 = [c for c in num2[::-1]]
        
                 
        n = len(num1)
        arr = [0] * (len(num2) + 1)
        print(arr)
        
        for i in range(n):
            value = int(carr1[i])  + int(carr2[i]) + arr[i]
            
            arr[i] = value % 10
            if value >= 10:
                arr[i+1] = 1
            
        # print(arr)
        res = ""
        
        for i in range(n, len(num2)):
            value = int(carr2[i]) + arr[i]
            arr[i] = value % 10 
            if value >=  10: 
                arr[i+1] = 1
        arr = arr[::-1]
        for i, c in enumerate(arr):
            res += str(c)
        
        if len(res) > 1 and res[0] == "0":
            return res[1:]
        return res
