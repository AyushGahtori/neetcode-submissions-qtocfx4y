from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        maap = {}
        
        def dfs(node):
            if node in maap:
                return maap[node]  # return the copy of that node to the below for loop
            copy = Node(node.val)
            maap[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))  # take this copy code then go to its neighbor list and append the return value from the dfs(i)
            return copy
        
        return dfs(node) if node else None
