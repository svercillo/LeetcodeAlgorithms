class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = "" 
        sorted_list = [
                {'k':'a','v': a},
                {'k':'b', 'v':b},
                {'k':'c', 'v':c}
        ]  
        
        sorted_list = sorted(sorted_list, key=lambda k: k['v'], reverse=True) 
        while (sorted_list[0]['v'] > 0 or sorted_list[1]['v'] >0 or sorted_list[2]['v'] >0):
            print(sorted_list, s)
            sorted_list = sorted(sorted_list, key=lambda k: k['v'], reverse=True) 
            
            
            # sub 2 from max 
            if ( 
                sorted_list[0]['v'] - sorted_list[1]['v'] >=2 
                and (len(s) == 0 or s[len(s)-1] != sorted_list[0]['k']) 
                and (sorted_list[0]['v'] >=2)
            ):
                s += f"{sorted_list[0]['k']}{sorted_list[0]['k']}"
                sorted_list[0]['v'] -= 2
            
            # sub 1 from max
            elif  (
                (len(s) <2 
                or not(s[len(s)-1] == sorted_list[0]['k'] and s[len(s)-2] == sorted_list[0]['k']))
                and (sorted_list[0]['v'] >=1)
            ):
                s += f"{sorted_list[0]['k']}"
                sorted_list[0]['v'] -= 1
                
            # sub 1 from second max
            elif (
                s[len(s)-1] != sorted_list[1]['k']  
                and  s[len(s)-2] != sorted_list[1]['k'] 
                and (sorted_list[1]['v'] >=1)
            ):
                sorted_list[1]['v'] -= 1
                s += f"{sorted_list[1]['k']}"

            # sub 1 from min
            elif (
                not (s[len(s)-1] == sorted_list[2]['k'] and s[len(s)-2] == sorted_list[2]['k'])
                and sorted_list[2]['v'] >=1 
            ):
                s += f"{sorted_list[2]['k']}"
                sorted_list[2]['v'] -= 1
                
            
            else: 
                return s
            
        return s
            
