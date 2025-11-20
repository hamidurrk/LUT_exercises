class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [set() for _ in range(n)]
    
    def add(self, u, v):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.adj_list[u].add(v)
            self.adj_list[v].add(u)
    
    def remove(self, u, v):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.adj_list[u].discard(v)
            self.adj_list[v].discard(u)
    
    def dft(self, start):
        visited = [False] * self.n
        result = []
        
        def dfs(vertex):
            visited[vertex] = True
            result.append(vertex)
            
            for neighbor in sorted(self.adj_list[vertex]):
                if not visited[neighbor]:
                    dfs(neighbor)
        
        dfs(start)
        print(' '.join(map(str, result)))


if __name__ == "__main__":
    graph = Graph(6)
    vertices = ((0, 2), (0, 4), (2, 1),
                   (2, 3), (2, 5), (3, 0),
                   (3, 5), (4, 5), (5, 1))
    for u, v in vertices:
        graph.add(u, v)
        
    graph.dft(0)

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)
