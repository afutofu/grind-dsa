def dfs(graph, start):
    # Initialize a set to keep track of visited nodes
    # Initialize a queue to keep track of nodes to visit
    visited = set()
    found = []

    # Add the starting node to the queue and mark it as visited
    found.append(start)
    visited.add(start)

    # While there are nodes to visit
    while not len(found) == 0:

        # Get the current node from the queue
        current = found.pop()

        # Print the current node
        print(current, end=" ")

        # Add all neighbors of the current node to the queue
        for neighbor in graph[current]:

            # If the neighbor has not been visited, mark it as visited and add it to the queue
            if neighbor not in visited:
                visited.add(neighbor)
                found.append(neighbor)


if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [2, 3],
        3: [5],
        4: [3, 5],
        5: [2],
    }

    print("DFS traversal:")
    dfs(graph, 1)
    print()
