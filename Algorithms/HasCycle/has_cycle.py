seen = set()
done = set()


def has_cycle(graph, curr):
    print(curr, end=" ")
    seen.add(curr)
    cycleFound = False
    for neighbor in graph[curr]:
        if neighbor in seen and neighbor not in done:
            print("Cycle detected!")
            cycleFound = True
        if neighbor not in seen and not cycleFound:
            cycleFound = has_cycle(graph, neighbor)

    done.add(curr)
    return cycleFound


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [5],
        3: [4, 6],
        4: [6],
        5: [8],
        6: [4, 7],
        7: [2],
        8: [7],
        9: [7, 8],
    }

    print("DFS traversal:")
    has_cycle(graph, 1)
    print()
