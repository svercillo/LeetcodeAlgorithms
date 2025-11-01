class Solution:
    def calculate(self, s: str) -> int:        
        s = "".join([c for c in s if c != " "])
    
        lastsim = "+"
        lastop = "*"

        runningp = 1
        runnings = 0
        
        currnum = []
        for c in s:
            if c in ["+", "-", "/", "*"]: 

                value = int("".join(currnum))
                # print(value, runningp, runnings)

                if lastop == "/":
                    if runningp > 0:
                        runningp = math.floor(runningp / value)
                    else:
                        runningp = math.ceil(runningp / value)
                elif lastop == "*":
                    runningp *= value
                elif lastop == "+":
                    runningp = value
                elif lastop == "-":
                    runningp = -value

                
                if c in ["+", "-"]:
                    runnings += runningp
                    runningp = 1

                lastop = c
                currnum = []
            else:
                currnum.append(c)



        value = int("".join(currnum))
        print(value, runningp,  3 // 2, runnings, "sdfsdf")

        if lastop == "/":
            if runningp > 0:
                runningp = math.floor(runningp / value)
            else:
                runningp = math.ceil(runningp / value)
        elif lastop == "*":
            runningp *= value
        elif lastop == "+":
            runningp = value
        elif lastop == "-":
            runningp = -value

        print(runnings, "SDFSDF", value, runningp)
        runnings += runningp
        runningp = 1
        print(runnings)

        
        print(runnings, runningp)
        

        

        return runnings
