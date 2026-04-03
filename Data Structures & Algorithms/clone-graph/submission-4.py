"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# undirected graph mean we can travel in both directions
# we have to create a deep copy
# use a hashmap with a dfs going all the way in one disrectoon bevause all the node is connected to each other.

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldtoNew = {} # A hashmap to map each node in the orignal graph to its clone

        def dfs(node):
            if node in OldtoNew: # if the node alredy exist in the hashmap return its clone immediatly to privent infinite loop.
                return OldtoNew[node]
            copy = Node(node.val)
            OldtoNew[node] = copy

            # The for loop goes through each neighbor of the original node (e.g., node1).
            # If node1 has neighbors node2 and node4, the loop will run twice—once for each neighbor.
            for i in node.neighbors:

                # The returned cloned neighbor from dfs(nei) is appended to copy.neighbors,
                # which is the neighbors list of the cloned version of the original node.
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node) if node else None          



        