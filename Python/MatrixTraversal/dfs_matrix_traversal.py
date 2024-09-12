def dfs(matrix, i, j, visited):
    rows = len(matrix)
    cols = len(matrix[0])

    # base case
    if i < 0 or j >= rows or j < 0 or j >= cols or visited[i][j]:
        return

    visited[i][j] = True
    print(matrix[i][j], end=' ')

    # explore in all four directions: up, down, left, right
    dfs(matrix, i-1, j, visited)
    dfs(matrix, i+1, j, visited)
    dfs(matrix, i, j-1, visited)
    dfs(matrix, i, j+1, visited)


def dfs_traversal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Traverse starting from (0, 0) for the whole matrix
    dfs(matrix, 0, 0, visited)
