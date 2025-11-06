import heapq

def dijkstra(graph, start):
    # početne udaljenosti — beskonačnost osim za start
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # prioritetni red (udaljenost, čvor)
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # preskoči ako već postoji bolji put
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # ako je novi put kraći — ažuriraj i dodaj u red
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# primjer grafa i poziva funkcije
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}
