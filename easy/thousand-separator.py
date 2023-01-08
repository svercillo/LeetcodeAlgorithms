class Solution:
    def thousandSeparator(self, num: int) -> str: 
        string = str(num)
        
        n = len(string)

        if n >= 4:            
            res = ""

            start = 0
            if n % 3 != 0: 
                # append leading
                res += string[:n%3]
                start += n%3 

            while start < n : 
                if start != 0:
                    res += "."
                res += string[start: start + 3]
                start += 3 

            return res
        else:
            return string
            