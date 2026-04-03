class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = {i:[] for i in range(n)}
        for a, b in edges:
            components[a].append(b)
            components[b].append(a)

        visited = set()
        conn_comp = 0

        def dfs(node):
            visited.add(node)

            for nei in components[node]:
                if nei not in visited:
                    dfs(nei)    

        for i in range(n):
            if i not in visited:
                conn_comp += 1
                dfs(i)

        return conn_comp              
