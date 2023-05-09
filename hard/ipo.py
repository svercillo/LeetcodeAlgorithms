class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        class Project:
            def __init__(self, index):
                self.index = index

            def __lt__(self, other):  

                
                return profits[self.index] > profits[other.index]

            def __repr__(self):
                return f"Project<{self.index}>"

        n = len(profits)
        projects = []
        for i in range(n):
            projects.append(Project(i))

        projects.sort(key = lambda proj : (capital[proj.index], profits[proj.index]))
        project_ind = 0
        heap = []


        

        added_project = True
        while k > 0 and (added_project or len(heap)):
            
            added_project = False
            while project_ind < n and w >= capital[projects[project_ind].index]:
                heapq.heappush(heap, projects[project_ind])
                project_ind += 1
                added_project = True
            
            if len(heap):
                top = heapq.heappop(heap)
                w += profits[top.index]
                k -= 1
   
        return w
