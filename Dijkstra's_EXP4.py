import heapq


def dijkstra(graph, source):
    n = len(graph)

    distance = [float("inf")] * n
    previous = [None] * n
    visited = set()

    distance[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:
            new_distance = distance[u] + weight

            if new_distance < distance[v]:
                distance[v] = new_distance
                previous[v] = u
                heapq.heappush(
                    priority_queue,
                    (new_distance, v)
                )

    return distance, previous


def reconstruct_path(previous, source, target):
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = 0

distance, previous = dijkstra(graph, source)

print(f"Shortest paths from vertex {source}:")
print(f'{"Vertex":>8} {"Distance":>10} {"Path":>30}')
print("-" * 55)

for vertex in range(len(graph)):
    path = reconstruct_path(
        previous,
        source,
        vertex
    )

    if path:
        path_string = " -> ".join(map(str, path))
    else:
        path_string = "No path"

    if distance[vertex] == float("inf"):
        value = "INF"
    else:
        value = distance[vertex]

    print(
        f"{vertex:>8} "
        f"{str(value):>10} "
        f"{path_string:>30}"
    )