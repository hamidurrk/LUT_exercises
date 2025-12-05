import heapq
def salesman(city_map):

    n = len(city_map)
    best_cost = float('inf')
    best_path = []

    min_out = [min([city_map[i][j] for j in range(n) if i != j]) for i in range(n)]

    def branch_and_bound(path, visited, current_cost):
        nonlocal best_cost, best_path

        if len(path) == n:
            total_cost = current_cost + city_map[path[-1]][path[0]]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path[:]
            return

        lower_bound = current_cost
        for i in range(n):
            if not visited[i]:
                lower_bound += min_out[i]
        if lower_bound >= best_cost:
            return

        for next_city in range(n):
            if not visited[next_city]:
                visited[next_city] = True
                path.append(next_city)
                branch_and_bound(path, visited, current_cost + city_map[path[-2]][next_city])
                path.pop()
                visited[next_city] = False

    visited = [False] * n
    visited[0] = True
    branch_and_bound([0], visited, 0)
    return best_path + [0]

if __name__ == "__main__":
    cost = 0
    city_map = [
        [ 0, 12, 19, 16, 29],
        [12,  0, 27, 25,  5],
        [19, 27,  0,  8,  4],
        [16, 25,  8,  0, 14],
        [29,  5,  4, 14,  0]
    ]
    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    print(path)
    print(cost)