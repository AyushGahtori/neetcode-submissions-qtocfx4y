class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
       
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False  
            if crs == []:
                return True
            visit.add(crs)

            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False
            visit.remove(crs)
            adj[crs] == []
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True                    
                    
