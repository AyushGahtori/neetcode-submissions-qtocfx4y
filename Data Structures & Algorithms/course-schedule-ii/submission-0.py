class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()   
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True # we dont need to visit is twice 
            cycle.add(crs) 
            for pre in prereq[crs]:
                if dfs(pre) == False: # cycle detected
                    return False
            # if all the prereq returns True
            cycle.remove(crs)

            # Mark course as fully processed (visited) 
            visit.add(crs) # visited this node add checked all its prereq and this course can be completed.   
            
            # Add course to output since all prerequisites are met.
            output.append(crs) # we can add it because we just went through all its prereq and from those prereq we added them to our output
            # this will add a course after we added its prereq
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output        
        