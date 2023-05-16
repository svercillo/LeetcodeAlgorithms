class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:


        fib = [1, 1]
        while fib[-1] <= k:
            fib.append(fib[-2] + fib[-1])

        finished = False
        mpath_len = math.inf

        def dfs(remaining, path_len):
            nonlocal mpath_len
            if mpath_len != math.inf:
                return True


            print(remaining, path_len)

            if remaining == 0:

                mpath_len = min(mpath_len, path_len)
                return True

            fib_ind = bisect.bisect_left(fib, remaining)

            # print(fib_ind)

            while fib_ind >= 0:
                # print(remaining, fib_ind)

                if remaining - fib[fib_ind] >= 0 and dfs(remaining - fib[fib_ind], path_len + 1):
                    return mpath_len

                fib_ind -= 1
                

            return False
        
        return dfs(k, 0)
