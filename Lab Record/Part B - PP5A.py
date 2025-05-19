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

    def bfs(self, start):
        visited = set()
        queue = [start]
        self._bfs_util(queue, visited)
        
    def _bfs_util(self, queue, visited):
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" -> ")
                visited.add(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)

graph.bfs(0)
