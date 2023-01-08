class Solution:
    def validWordSquare(self, words) -> bool:
        n = len(words)
        for word in words: 
            if len(word) > n:
                n = len(word)
        

        mat = words

        words = [] 
        last_len = n

        for i in range(n):
            if i >= len(mat):
                arr = [" " for _ in range(n)]
                words.append(arr)
                continue 

            word = mat[i]
            arr = list(word)  
            if len(arr) > last_len:
                print("AAAA")
                return False
            for _ in range(n - len(arr)):
                arr.append(" ")

            last_len = len(arr)
            words.append(arr)

        # print(words)        

        for i in range(n):
            for j in range(n):
                if words[i][j] == " ":
                    if words[j][i] != " ":
                        # print("BBBB")
                        return False


            

        print(words)
        
        for i in range(n):
            # print()
            for j in range(0, n -i):
                

                # print(i, i +j)
                
                # print(words[i+ j][i], words[i][i + j])
                if words[i+ j][i] != words[i][i + j]:
                    return False
                
        return True
        
