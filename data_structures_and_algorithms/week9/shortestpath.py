import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]
    
    def add(self, u, v, w):
        if 0 <= u < self.n and 0 <= v < self.n:
            self.adj_list[u].append((v, w))
    
    def shortest_path(self, start, end):
        dist = [float('inf')] * self.n
        dist[start] = 0
        
        parent = [-1] * self.n
        
        pq = [(0, start)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > dist[u]:
                continue
            
            if u == end:
                break
            
            for v, weight in self.adj_list[u]:
                new_dist = dist[u] + weight
                
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    heapq.heappush(pq, (new_dist, v))
        
        if dist[end] == float('inf'):
            print(-1)
        else:
            path = []
            current = end
            while current != -1:
                path.append(current)
                current = parent[current]
            path.reverse()
            print(' '.join(map(str, path)))


if __name__ == "__main__":
    graph = Graph(10)
    edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
                   (1, 4,  3), (2, 3,  7), (2, 5, 25),
                   (3, 4, 12), (3, 5, 15), (3, 6,  4),
                   (3, 7, 15), (3, 8, 20), (4, 7,  2),
                   (5, 8,  2), (6, 7,  8), (6, 8, 13),
                   (6, 9, 15), (7, 9,  5), (8, 9,  1))
    for u, v, w in edges:
        graph.add(u, v, w)

    graph.shortest_path(0, 9)
