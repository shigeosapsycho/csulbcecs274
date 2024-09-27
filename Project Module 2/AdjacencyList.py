"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i].append(j)

    def remove_edge(self, i: int, j: int):
        if j in self.adj[i]:
            self.adj[i].remove(j)
                
    def has_edge(self, i : int, j: int) ->bool:
        return j in self.adj[i]
        
    def out_edges(self, i) -> List:
        # todo
        pass

    def in_edges(self, i) -> List:
        # todo
        edges = []
        for j in range(self.n):  # Traverse all nodes
            if i in self.adj[j]:  # If node i is in the adjacency list of node j, it's an incoming edge
                edges.append(j)
        return edges
    
    def bfs(self, r : int, dest: int):
        visited = [False] * self.n
        queue = []
        queue.append(r)
        visited[r] = True
        
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            
            for v in self.adj[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

    def dfs(self, r : int, dest: int):
        visited = [False] * self.n
        stack = []
        stack.append(r)

        while stack:
            u = stack.pop()
            if not visited[u]:
                print(u, end=" ")
                visited[u] = True

                for v in reversed(self.adj[u]):
                    if not visited[v]:
                        stack.append(v)
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s




