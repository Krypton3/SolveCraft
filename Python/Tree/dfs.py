def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    # add the root node to visited
    visited.add(node)
    print(node, end=' ')

    # exploring the neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_stack(graph, start):
    # track of visited node
    visited = set()
    # using stack for DFS
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)


# graph
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# Start DFS from node 1
print("DFS Recursive Traversal: ", end='')
dfs_stack(graph, 1)
