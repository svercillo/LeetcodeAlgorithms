class Solution:
    def numDecodings(self, s: str) -> int:
        
        visited = {}

        def nways(indx):
            if indx in visited:
                return visited[indx]
            elif indx == len(s):
                visited[indx] = 1
            elif s[indx] == '0':
                visited[indx] = 0
            else: 
                res = 0 
                if indx +2  <= len(s):
                    if int(s[indx: indx +2]) <= 26:
                        res = nways(indx+2)

                res += nways(indx+1)

                visited[indx] = res
            
            return visited[indx]
        
        return nways(0)
