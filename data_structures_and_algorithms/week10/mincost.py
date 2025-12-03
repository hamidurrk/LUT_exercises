class Graph:
	def __init__(self, n):
		self.n = n
		self.edges = set()  

	def add(self, u, v, w):
		if u > v:
			u, v = v, u
		self.edges.discard((u, v, w))  
		for e in list(self.edges):
			if e[0] == u and e[1] == v:
				self.edges.remove(e)
		self.edges.add((u, v, w))

	def remove(self, u, v):
		if u > v:
			u, v = v, u
		for e in list(self.edges):
			if e[0] == u and e[1] == v:
				self.edges.remove(e)

	def min_cost(self):
		parent = list(range(self.n))
		def find(u):
			while parent[u] != u:
				parent[u] = parent[parent[u]]
				u = parent[u]
			return u
		def union(u, v):
			pu, pv = find(u), find(v)
			if pu == pv:
				return False
			parent[pu] = pv
			return True
		mst_weight = 0
		edge_count = 0
		for u, v, w in sorted(self.edges, key=lambda x: x[2]):
			if union(u, v):
				mst_weight += w
				edge_count += 1
				if edge_count == self.n - 1:
					break
		if edge_count != self.n - 1:
			return -1  
		return mst_weight


if __name__ == "__main__":
	graph = Graph(6)
	edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
				   (2, 3, 1), (2, 5, 2), (3, 0, 6),
				   (3, 5, 2), (4, 5, 1), (5, 1, 6))
	for u, v, w in edges:
		graph.add(u, v, w)

	print(graph.min_cost())

	graph.remove(2, 3)

	print(graph.min_cost())
