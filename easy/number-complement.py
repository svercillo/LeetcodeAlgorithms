class Solution:
    def findComplement(self, num: int) -> int:
        s = str(bin(num))
        print(s)
        print(s[2:])
            
            
        string = ""
        for i in s[2:]:
            if i == "0":
                string += "1"
            else: 
                string += "0"
            

        
        return int(string, 2)
