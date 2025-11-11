class Solution:
    def validIPAddress(self, string: str) -> str:
        invalid = "Neither"
        if "." in string and ":" in string: 
            return invalid

        def ip4(string):
            values = string.split(".")

            if len(values) != 4:
                return invalid

            for v in values:
                if len(v) > 1 and v[0] == "0" or 0 == len(v) or len(v) > 3:
                    return invalid
                for c in v:
                    if not c.isdigit():
                        return invalid
                if int(v) > 255:
                    return invalid
            
            return "IPv4"

        def ip6(string):
            values = string.split(":")
            print("sfwef")

            if len(values) != 8:
                return invalid

    
            
            
            for v in values:
                if not (1 <=  len(v) <5):
                    return invalid
                for c in v:
                    if not c.isdigit() and not c.isalpha():
                        return invalid

                    if c.isalpha(): 

                        if not(97 <= ord(c.lower())  < 103):
                            return invalid
            return "IPv6"    
            

        if "." in string:
            return ip4(string)

        return ip6(string)
        

        
