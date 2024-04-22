from priority_queue import PriorityQueue


def dijksras(graph, start, end):
    distances = [float("inf") for _ in graph]
    done = [False for _ in graph]

    pq = PriorityQueue()
    pq.insert(0, start)

    distances[start] = 0

    while not pq.is_empty():
        current = pq.delete_min()
        done[current.value] = True
        print(current.value, end=" ")

        for neighbor, weight in graph[current.value]:
            if not done[neighbor]:
                new_weight = distances[current.value] + weight

                # If the weight is infinity, insert the neighbor into the priority queue
                if distances[neighbor] == float("inf"):
                    pq.insert(new_weight, neighbor)

                # If the new weight is less than the current weight, update the weight
                if new_weight < distances[neighbor]:
                    distances[neighbor] = new_weight
                    pq.decrease_key(new_weight, neighbor)

    return distances[end]


if __name__ == "__main__":
    graph = {
        0: [(1, 10), (2, 12)],
        1: [(0, 10), (2, 9), (4, 8)],
        2: [(1, 9), (3, 3), (5, 1)],
        3: [(2, 3), (4, 7), (5, 3)],
        4: [(1, 8), (3, 7), (6, 5), (7, 6)],
        5: [(2, 1), (3, 3), (6, 7)],
        6: [(4, 5), (5, 7), (7, 9), (8, 11)],
        7: [(4, 6), (6, 9), (8, 2)],
        8: [(6, 11), (7, 2)],
    }

    start = 0
    end = 8

    shortest_path = dijksras(graph, start, end)

    print(f"\nThe shortest path from {start} to {end} is {shortest_path}")
