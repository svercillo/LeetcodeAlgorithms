class Solution:
    def minChanges(self, n: int, k: int) -> int:
        

        bin_n = bin(n)[2:][::-1]
        bin_k = bin(k)[2:][::-1]

        if len(bin_n) < len(bin_k): 
            return -1



        num_changes = 0
        for i in range(len(bin_k)): 
            if bin_n[i] == '0' and bin_k[i] == '1':
                return -1

            elif bin_n[i] == '1' and bin_k[i] == '0':
                num_changes += 1 

        print((bin_n, bin_k), num_changes)


        for i in range(len(bin_k), len(bin_n)): 
            if bin_n[i] == '1':
                num_changes += 1


        return num_changes  
