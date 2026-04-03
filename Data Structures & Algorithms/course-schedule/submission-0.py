class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course with prereq list
        premap = {i: [] for i in range(numCourses)}  # Initialize premap with an empty list for each course
        for c, p in prerequisites:
            premap[c].append(p)  

        # visitSet = all courses along with the DFS path
        visitset = set()

        def dfs(c):
            if c in visitset:  # visiting a same course twice
                return False  # we detected a loop
            if premap[c] == []:
                return True

            visitset.add(c)  # currently visiting this course

            # check every prerequisite of this course to see if they can be completed.
            for p in premap[c]:
                if not dfs(p):  # if this returns False, it means we cannot finish this course.
                    return False  # we return False

            ## Remove from visitset to backtrack, preventing false cycle detection in other DFS paths.        
            visitset.remove(c)

            # this will save us time; we don't have to run dfs on its neighbors.
            premap[c] = []  # we checked that we can finish every prereq of this course, so make it an empty list BaseCase.
            return True  # every prerequisite of this course can be completed

        # 1 -> 2
        # 3 -> 4 
        # these two separate graphs are not connected
        # so we have to use this for loop
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
