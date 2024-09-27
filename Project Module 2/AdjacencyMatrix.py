from Interfaces import Graph, List
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n*n)

    def add_edge(self, i: int, j: int):
        self.adj[i * self.n + j] = 1

    def remove_edge(self, i: int, j: int):
        self.adj[i * self.n + j] = 0

    def has_edge(self, i: int, j: int) -> bool:
        return self.adj[i * self.n + j] == 1
    
    def out_edges(self, i) -> List:
        edges = []
        for j in range(self.n):
            if self.adj[i][j] == 1:  # If there's an edge from i to j, add j to the list
                edges.append(j)
        return edges

    def in_edges(self, i) -> List:
        # todo
        edges = []
        for j in range(self.n):
            if self.adj[j][i] == 1:  # If there's an edge from j to i, add j to the list
                edges.append(j)
        return edges

    def bfs(self, r : int):
        # todo
        visited = [False] * self.n
        queue = []
        queue.append(r)
        visited[r] = True
        
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            
            for v in range(self.n):
                if self.adj[u][v] == 1 and not visited[v]:  # If there's an edge and v hasn't been visited
                    queue.append(v)
                    visited[v] = True

    def dfs(self, r : int):
        # todo
        visited = [False] * self.n
        stack = []
        stack.append(r)

        while stack:
            u = stack.pop()
            if not visited[u]:
                print(u, end=" ")
                visited[u] = True

                for v in range(self.n - 1, -1, -1):  # Traverse in reverse order for correct DFS
                    if self.adj[u][v] == 1 and not visited[v]:
                        stack.append(v)

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s



