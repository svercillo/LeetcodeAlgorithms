
class Solution:
    
    def removeSpaces(self, s) -> str: 
        temp = [] 
        for c in s:
            if c != " ":
                temp.append(c)
                
        return "".join(temp)
    
    def generateBracketMap(self, s): 
        bracketMap = {}
        stack = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                start = stack.pop() 
                bracketMap[start] = i
                
        return bracketMap

    
    def calculate(self, s) -> int:
        s = self.removeSpaces(s)
        n = len(s)
        
        bracketMap = self.generateBracketMap(s)

        
        def evaluate(start, end): # start, end inclusive
            ind = start
            
            res = 0
            
            currNum = ""
            op = "+"
            while ind <= end:
                if ind in bracketMap:
                    innerStart = ind + 1 
                    innerEnd = bracketMap[ind] - 1
                    evalRes = evaluate(innerStart, innerEnd)
                    res += evalRes if op == "+" else -evalRes
                    
                    ind = innerEnd + 2 
                elif s[ind] in ["+", "-"]:
                    op = s[ind]
                    ind += 1
                else:
                    currNum += s[ind]

                    if ind == end or s[ind+1] in ["+", "-"]:
                        intVal = int(currNum)
                        res += intVal if op == "+" else -intVal
                        currNum = ""
                    ind += 1
            return res
                        
        return evaluate(0, n -1)
                    
