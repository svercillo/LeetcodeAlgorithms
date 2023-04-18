from pprint import pprint
class Solution:
    def sumSubarrayMins(self, arr) -> int:

        global_sum = 0
        class Number:
            start = 0
            end = 0
            val = 0
            def __init__(self, index, val):
                self.index = index
                self.val = val

            
            def __repr__(self):
                return f"Num<val: {self.val}, start: {self.start}, index: {self.index},  end: {self.end}>"
        
        nodes = {}
        stack = []

        for i, e in enumerate(arr):
            while len(stack) and e <= stack[-1].val:
                top = stack.pop()
                if len(stack) > 0:
                    top.start = stack[-1].index + 1 # element is less than e
                else:
                    top.start = 0
                top.end = i

            number = Number(i, e)
            stack.append(number)
            nodes[number.val] = number


        while len(stack):
            top = stack.pop()
            if len(stack):
                top.start = stack[-1].index + 1 # element is less than e
            else:
                top.start = 0
            top.end = len(arr)

        pprint(nodes)
        total_sum = 0
        for k in nodes:
            if nodes[k].index == 0:
                added = k * (nodes[k].end - nodes[k].index)
            elif nodes[k].index == len(arr) -1 :     
                added = k * (nodes[k].index - nodes[k].start + 1)
            else:
                added = k * (nodes[k].index - nodes[k].start + 1) * (nodes[k].end - nodes[k].index)


            total_sum += added



        return total_sum

# res = Solution().sumSubarrayMins([3,1,2,4])
# res = Solution().sumSubarrayMins([11,81,94,43,3])
# res = Solution().sumSubarrayMins([1,2,5,4,3])
res = Solution().sumSubarrayMins([1,2,3,2, 1])

print(res)
