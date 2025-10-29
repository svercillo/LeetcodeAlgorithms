class Solution:
    def countPairs(self, nums: List[int]) -> int:

        def almostEqualPair(a, b):
            if a > b: 
                t = a
                a = b 
                b = t

            diff = len(str(b)) - len(str(a))
            a = "0" * diff + str(a)
            b = str(b)

            if a == b:
                return True
            
    
            for i in range(len(a)-1 ):
                for j in range(i + 1, len(a)): 
                    # try to swap 
                    char_arr = list(a)

                    t = a[i] 
                    char_arr[i] = char_arr[j]
                    char_arr[j] = t
                    

                    if "".join(char_arr) == b: 
                        return True

            return False


            


        count = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i +1, n):
                a = nums[i]
                b = nums[j]

                # print(a, b)
                if almostEqualPair(a, b):
                    count += 1




        return count
                


