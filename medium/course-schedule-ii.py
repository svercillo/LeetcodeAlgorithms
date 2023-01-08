from pprint import pprint


class Solution:
    def findOrder(self, numCourses: int, prerequisites):

        self.conns = {}
        self.status = {}
        self.res = []
        self.invalid = False

        for i in range(numCourses):
            self.conns[i] = set()
            self.status[i] = 0

        for a, b in prerequisites:
            self.conns[a].add(b)

        for i in range(numCourses):
            self.dfs(i)

        if self.invalid:
            return []

        return self.res

    def dfs(self, val):
        if self.status[val] == 2:
            return

        elif self.status[val] == 1:
            self.invalid = True
            return

        self.status[val] = 1

        for e in self.conns[val]:
            self.dfs(e)

        self.res.append(val)
        self.status[val] = 2


res = Solution().findOrder(7, [[1, 0]])

print(res)
