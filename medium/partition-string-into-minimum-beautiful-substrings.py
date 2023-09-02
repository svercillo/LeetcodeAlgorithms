class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        

        n = len(s)


        @cache
        def isPowerOf5(string):
            x = int(string, 2)

            if x == 1:
                return True
            
            while x % 5 == 0:
                x /= 5
            return x == 1

    
        # @cache
        def minPartitions(start) -> int: 

            if start == n:
                return 0

        
            if s[start] == "0":
                return math.inf

            buffer = []
            smallest_num = math.inf
            end = start

            # print(start)
            while end < len(s):
                buffer.append(s[end])
                
                if isPowerOf5("".join(buffer)):
                    print((start,end ), "".join(buffer))
                    min_next =  minPartitions(end + 1)
                    smallest_num = min(min_next + 1, smallest_num)
                end += 1
            return smallest_num


        res = minPartitions(0)
        if res == math.inf: 
            return -1
        else:
            return res
