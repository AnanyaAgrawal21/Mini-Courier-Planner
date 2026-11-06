
import heapq

# Mini-Courier Planner - Phase 3
# Graph, Dijkstra's Algorithm, Nearest-Neighbor TSP

# 1. Weighted graph: each road has a distance
graph = {
    "A": {"B": 4, "C": 2, "D": 7},
    "B": {"A": 4, "C": 1, "D": 5, "E": 7},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"A": 7, "B": 5, "C": 8, "E": 2},
    "E": {"B": 7, "C": 10, "D": 2}
}

# 2. Dijkstra: shortest distances and paths from source
def dijkstra(graph, source):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, current = heapq.heappop(pq)

        if current_distance > distances[current]:
            continue

        for neighbor, weight in graph[current].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(pq, (new_distance, neighbor))

    return distances, previous


def build_path(previous, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1]


# 3. Print shortest paths from A
print("DIJKSTRA SHORTEST PATHS FROM A")
distances, previous = dijkstra(graph, "A")

for destination in graph:
    path = build_path(previous, destination)
    print(f"A -> {destination}: {' -> '.join(path)}, "
          f"Distance = {distances[destination]}")


# 4. Nearest-Neighbor TSP approximation
def nearest_neighbor_tsp(graph, start):
    unvisited = set(graph.keys())
    unvisited.remove(start)

    route = [start]
    total_distance = 0
    current = start

    while unvisited:
        reachable = [
            (graph[current][neighbor], neighbor)
            for neighbor in unvisited
            if neighbor in graph[current]
        ]

        if not reachable:
            raise ValueError("Not all locations are reachable.")

        distance, next_node = min(reachable)
        total_distance += distance
        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    # Return to starting point if a road exists
    if start in graph[current]:
        total_distance += graph[current][start]
        route.append(start)

    return route, total_distance


# 5. Print approximate delivery tour
print("\nNEAREST-NEIGHBOR DELIVERY ROUTE")
route, total_distance = nearest_neighbor_tsp(graph, "A")

print("Route:", " -> ".join(route))
print("Total route distance:", total_distance)
