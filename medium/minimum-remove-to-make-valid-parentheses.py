class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        n = len(s)

        q = []
        starting_store = {}
        ending_store = {}
        i = 0
        while i < n:
            j = i
            while j < n and s[j] not in set(["(", ")"]):
                j += 1

            if j - i >= 0:
                q.append((i,j))
                
                starting_store[i] = j

                if j not in ending_store: 
                    ending_store[j] = set()
                ending_store[j]= i

            i = j + 1

            
        def expand(start, end):
            if start not in starting_store:
                return # this interval has already been combined 
            init_start = start
            init_end = end

            # expand as large as you can
            while start -1 >= 0 and end < n and s[start-1] == "(" and s[end] == ")":
                start -=1
                end += 1

            starting_store.pop(init_start)
            ending_store.pop(init_end)

            # combine all the intervals that you can 
            while start in ending_store:
                new_start = ending_store[start]
                ending_store.pop(start)
                start = new_start

            while end in starting_store:
                new_end = starting_store[end]
                starting_store.pop(end)
                end = new_end

            # store final state after combining
            starting_store[start] = end
            ending_store[end] = start

            if (start, end) != (init_start, init_end):
                expand(start, end)


        for start, end in q:
            expand(start, end)

        merged_intervals = sorted([(start, starting_store[start]) for start in starting_store])
        res = []
        for start, end in merged_intervals:
            
            for i in range(start, end):
                res.append(s[i])

        return "".join(res)

            

            

