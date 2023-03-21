class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(lambda : set()) # contains all the courses a course is a prereq to  

        for prereq, course in prerequisites:
            graph[prereq].add(course)

        path = set()


        @cache
        def courses_that_need_req(course): # returns a set of all the courses that need 'course' as a prereq
            if course in path:
                return set()

            result = set([course])
            path.add(course)
            for v in graph[course]:
                result = result.union(courses_that_need_req(v))
            
            path.remove(course)


            return result

        res = []
        for prereq, course in queries:
            res.append(course in courses_that_need_req(prereq))


        return res
