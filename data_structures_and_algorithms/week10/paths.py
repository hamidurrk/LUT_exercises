class Graph:
	def __init__(self, n):
		self.n = n
		self.adj = [{} for _ in range(n)]  

	def add(self, u, v, w):
		self.adj[u][v] = w

	def remove(self, u, v):
		if v in self.adj[u]:
			del self.adj[u][v]

	def all_paths(self):
		n = self.n
		dist = [[float('inf')] * n for _ in range(n)]
		for i in range(n):
			dist[i][i] = 0
			for v, w in self.adj[i].items():
				dist[i][v] = w
		for k in range(n):
			for i in range(n):
				for j in range(n):
					if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
						if dist[i][j] > dist[i][k] + dist[k][j]:
							dist[i][j] = dist[i][k] + dist[k][j]
		for i in range(n):
			for j in range(n):
				if dist[i][j] == float('inf'):
					dist[i][j] = -1
		return dist


if __name__ == "__main__":
	graph = Graph(6)
	edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
				   (2, 3, 1), (2, 5, 2), (3, 0, 6),
				   (3, 5, 2), (4, 5, 1), (5, 1, 6))
	for u, v, w in edges:
		graph.add(u, v, w)

	M = graph.all_paths()
	for weights in M:
		for weight in weights:
			print(f"{weight:3d}", end="")
		print()
