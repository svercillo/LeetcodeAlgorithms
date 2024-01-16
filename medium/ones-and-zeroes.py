class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ''' 
        ideas:
            convert all the strings into freq tuple 
            sort based on nones then nzeors
            dp recursion:
                max number at i = max number at i + 1 + take or not


        ''' 

        freq_list = []
        for i, string in enumerate(strs):
            nones = 0
            nzeros = 0
            for c in string:
                if c == "1":
                    nones += 1
                else:
                    nzeros += 1
            freq_list.append((nzeros, nones))
        
        freq_list.sort() 

        @cache
        def largest_subset(i, m, n): 
            largest = 0

            if i == len(freq_list):
                return 0

            if m >= freq_list[i][0] and n >= freq_list[i][1]:
                largest = max(
                    largest,
                    1 + largest_subset(i+1, m - freq_list[i][0], n - freq_list[i][1]), 
                )

            largest = max(largest, largest_subset(i+1, m, n))

            return largest
            

        return largest_subset(0, m, n)

    
