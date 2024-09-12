from collections import deque


def bfs(graph, root):
    # visited nodes, queue to implement FIFO
    visited = set()
    queue = deque([root])
    visited.add(root)

    while queue:
        # FIFO
        node = queue.popleft()
        print(node, end=' ')
        # exploring the neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def bfs_binary_tree(root):
    if root is None:
        return []
    queue = deque([root])
    while queue:
        # FIFO
        node = queue.popleft()
        print(node, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}
print("BFS Traversal:", end=" ")
bfs(graph, 1)
