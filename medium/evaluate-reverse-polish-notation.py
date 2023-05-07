import math
class Solution:
    def evalRPN(self, tokens) -> int: 
        stack = []
        for tok in tokens:
            if tok in {"+", "-", "*", "/"}:
                second = stack.pop()
                first = stack.pop()
                

                if tok == "+":
                    value = first + second
                elif tok == "-":
                    value = first - second
                elif tok == "*":
                    value = first * second
                elif tok == "/":
                    if first / second > 0:
                        value = math.floor(first / second)
                    else:
                        value = math.ceil(first / second)

                stack.append(value)
            else:
                value = int(tok)
                stack.append(value)

        

        return stack[-1]
    