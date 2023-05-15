class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        
        zipped = sorted(zip(username, timestamp, website), key =lambda k : k[1])
        user_usage = defaultdict(lambda : [])
        res = defaultdict(lambda : set())

        for i in range(n):
            user, _, website = zipped[i]
            user_usage[user].append(website)

        for uid, user in enumerate(user_usage):
            acts = user_usage[user]

            print(acts)
            path = []
            def dfs(index, acts, uid):
                
                if index == len(acts) or len(path) == 3:
                    return
                
                path.append(acts[index])
                if len(path) == 3:
                    res[tuple(path )].add(uid)
                dfs(index +1, acts, uid)
                path.pop()


                dfs(index+ 1, acts, uid)
            dfs(0, acts, uid)

            # break

        from pprint import pprint 
        pprint([(k,res[k]) for k in res])

        if not len(res):
            return []
        highest_freq = max([len(res[k]) for k in res])

        possible = []
        for k in res:
            if len(res[k]) == highest_freq:
                possible.append(k)

        possible.sort()




        return possible[0]
