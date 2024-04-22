seen = set()
done = set()


def has_cycle(graph, curr):
    print(curr, end=" ")
    seen.add(curr)
    for neighbor in graph[curr]:
        if neighbor not in seen:
            has_cycle(graph, neighbor)
        elif neighbor not in done:
            print("Cycle detected!")
            exit(0)
    done.add(curr)


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
