import heapq


# ---------- Union-Find for Kruskal ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


# ---------- Kruskal's Algorithm ----------
def kruskal(n, edges):
    edges = sorted(edges)
    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

        if len(mst) == n - 1:
            break

    return mst, total_cost


# ---------- Prim's Algorithm ----------
def prim(n, adjacency_list, start=0):
    visited = [False] * n
    min_heap = [(0, start, -1)]

    mst = []
    total_cost = 0

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)

        if visited[vertex]:
            continue

        visited[vertex] = True

        if parent != -1:
            mst.append((parent, vertex, weight))
            total_cost += weight

        for neighbour, edge_weight in adjacency_list[vertex]:
            if not visited[neighbour]:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbour, vertex)
                )

    return mst, total_cost


# ---------- Graph Definition ----------
number_of_vertices = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]


# Create adjacency list for Prim's algorithm
adjacency_list = [[] for _ in range(number_of_vertices)]

for weight, u, v in edges:
    adjacency_list[u].append((v, weight))
    adjacency_list[v].append((u, weight))


# Run both algorithms
kruskal_mst, kruskal_cost = kruskal(
    number_of_vertices,
    edges
)

prim_mst, prim_cost = prim(
    number_of_vertices,
    adjacency_list
)


# ---------- Display Results ----------
print("=== Kruskal's MST ===")

for u, v, weight in kruskal_mst:
    print(f"Edge ({u} - {v}) Weight: {weight}")

print(f"Total MST Cost: {kruskal_cost}")


print("\n=== Prim's MST ===")

for u, v, weight in prim_mst:
    print(f"Edge ({u} - {v}) Weight: {weight}")

print(f"Total MST Cost: {prim_cost}")


# Verify both costs
if kruskal_cost == prim_cost:
    print("\nBoth algorithms produce the same MST cost.")
else:
    print("\nThe MST costs are different.")
