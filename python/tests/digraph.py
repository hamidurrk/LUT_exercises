# create a digraph 

class DiGraph():
    def __init__(self):
        self.graph = {}
        self.nodes = {}
        self.edges = {}
        self.node_count = 0
        self.edge_count = 0

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
            self.nodes[u] = self.node_count
            self.node_count += 1
        if v not in self.graph:
            self.graph[v] = []
            self.nodes[v] = self.node_count
            self.node_count += 1
        self.graph[u].append(v)
        self.edges[(u, v)] = self.edge_count
        self.edge_count += 1
    
    def successors(self, u):
        return self.graph[u]

    def predecessors(self, u):
        predecessors = [node for node in self.graph if u in self.graph[node]]
        return predecessors

    def has_successor(self, u, v):
        return v in self.graph[u]
    
    def has_predecessor(self, u, v):
        return u in self.graph[v]
    
G = DiGraph()
G.add_edge(1, 2)
G.add_edge(2, 1)
G.add_edge(5, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

print(G.graph)
print(G.nodes)
print(G.edges)

print(G.predecessors(2))