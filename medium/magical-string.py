class Solution:
    def magicalString(self, n: int) -> int:
        # 1 22 11 2 1 22 1 22 11 2 11 22 

        if n <=3: 
            return 1

        nones = 1
        number = [1,  2, 2]
        p = 1

        i = 3
        while True:
            nxt = 2 if number[-1] == 1 else 1 
            for nf in [1, 2]: # frequency of next gap
                if number[p+ 1] == nf: 
                    for _ in range(nf):
                        nones += 1 if nxt == 1 else 0
                        # print("\tadding" ,nxt, nf)
                        number.append(nxt)
                        i += 1
                        if i == n:
                            return nones
                    p += 1
                    
                    break


        
        print(number)
        return nones

                
        
            

            

        

        

        '''
        states:
        last -> 1 -> 22 
        last -> 2 -> 1 
        last -> 11
        last -> 22
        ''' 
