class Graph:
	def __init__(self, n):
		self.n = n
		self.adj = [set() for _ in range(n)]

	def add(self, u, v):
		self.adj[u].add(v)
		self.adj[v].add(u)

	def remove(self, u, v):
		self.adj[u].discard(v)
		self.adj[v].discard(u)

	def subgraphs(self):
		visited = [False] * self.n
		def dfs(u):
			stack = [u]
			while stack:
				node = stack.pop()
				if not visited[node]:
					visited[node] = True
					for v in self.adj[node]:
						if not visited[v]:
							stack.append(v)
		count = 0
		for i in range(self.n):
			if not visited[i]:
				dfs(i)
				count += 1
		return count

if __name__ == "__main__":
	graph = Graph(6)

	edges = ((0, 4), (2, 1), (2, 5), (3, 0), (5, 1))
	for u, v in edges:
		graph.add(u, v)
	print(graph.subgraphs())

	more_edges = ((0, 2), (2, 3), (3, 5), (4, 5))
	for u, v in more_edges:
		graph.add(u, v)
	print(graph.subgraphs())
