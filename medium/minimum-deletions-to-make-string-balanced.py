class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        cache = []
        for _ in s:
            cache.append([-1, -1])

        def min_deletions(ind, first_letter):

            if ind == len(s):
                return 0


            # print(ind, int(first_letter))
            if cache[ind][int(first_letter)] != -1:
                return cache[ind][int(first_letter)]

            elif first_letter:
                if s[ind] == "a":
                    res = min_deletions(ind +1, True)
                else:
                    res = min(
                        min_deletions(ind + 1, True) +1,
                        min_deletions(ind + 1, False) 
                    )
            else:
                if s[ind] == "a":
                    res = min_deletions(ind + 1, False) + 1
                else:
                    res = min_deletions(ind + 1, False)
            
            cache[ind][int(first_letter)] = res
            return res

        return min(
            min_deletions(0, True),
            min_deletions(0, False)
        )
