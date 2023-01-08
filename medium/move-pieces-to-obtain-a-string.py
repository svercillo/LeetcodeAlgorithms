class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        start_l, start_r, targ_l, targ_r = [], [], [], []

        start_order = []
        target_order = []
        for i in range(n):
            if start[i] != "_":
                start_order.append(start[i])
            
                if start[i] == "L":
                    start_l.append(i)
                else:
                    start_r.append(i)

            if target[i] != "_":
                target_order.append(target[i])

                if target[i] == "L":
                    targ_l.append(i)
                else:
                    targ_r.append(i)

        if start_order != target_order:
            return False


        for i in range(len(start_l)):
            if start_l[i] < targ_l[i]:
                return False

        for i in range(len(targ_r)):
            if start_r[i] > targ_r[i]:
                return False

        return True
