# Use python queue module to implement a queue
import queue


def bfs(graph, start):
    # Initialize a set to keep track of visited nodes
    # Initialize a queue to keep track of nodes to visit
    visited = set()
    found = queue.Queue()

    # Add the starting node to the queue and mark it as visited
    found.put(start)
    visited.add(start)

    # While there are nodes to visit
    while not found.empty():

        # Get the current node from the queue
        current = found.get()

        # Print the current node
        print(current, end=" ")

        # Add all neighbors of the current node to the queue
        for neighbor in graph[current]:

            # If the neighbor has not been visited, mark it as visited and add it to the queue
            if neighbor not in visited:
                visited.add(neighbor)
                found.put(neighbor)


if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [2, 3],
        3: [5],
        4: [3, 5],
        5: [2],
    }

    print("BFS traversal:")
    bfs(graph, 1)
    print()
