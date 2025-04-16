class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start_vertex):
        visited = []
        self._dfs_util(start_vertex, visited)
    
    def _dfs_util(self, star_vertex, visited):
        visited.append(star_vertex)
        print(star_vertex, end="\n")
        for neighbor in self.adj_list:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.dfs(0)
