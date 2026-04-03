class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)

        cycle, visit = set(), set()
        output = []

        # visited = course has been added to the output
        # visiting = course added to cycle
        # unvisited = course has been added to none  

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output        




        