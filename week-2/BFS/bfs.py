import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "../Queue")

from queue import Queue


def bfs(graph, start):
    # Initialize a set to keep track of visited nodes
    # Initialize a queue to keep track of nodes to visit
    visited = set()
    found = Queue()

    # Add the starting node to the queue and mark it as visited
    found.enqueue(start)
    visited.add(start)

    # While there are nodes to visit
    while not found.is_empty():

        # Get the current node from the queue
        current = found.dequeue()

        # Print the current node
        print(current, end=" ")

        # Add all neighbors of the current node to the queue
        for neighbor in graph[current]:

            # If the neighbor has not been visited, mark it as visited and add it to the queue
            if neighbor not in visited:
                visited.add(neighbor)
                found.enqueue(neighbor)


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4],
    }

    print("BFS traversal:")
    bfs(graph, 0)
    print()
