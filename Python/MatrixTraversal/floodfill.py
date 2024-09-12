from collections import deque


def flood_fill_dfs(image, sr, sc, newColor):
    # using DFS
    original_color = image[sr][sc]

    # base condition: if it's already the same color
    if original_color == newColor:
        return image

    def dfs(i, j):
        # base condition: check other constraints
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or \
                image[i][j] != original_color:
            return
        # Change the color of the current cell
        image[i][j] = newColor

        # perform dfs to all possible directions
        dfs(i - 1, j)  # Up
        dfs(i + 1, j)  # Down
        dfs(i, j - 1)  # Left
        dfs(i, j + 1)  # Right
    dfs(sr, sc)
    return image


def flood_fill_bfs(image, sr, sc, newColor):
    original_color = image[sr][sc]

    # base condition: if it's already the same color
    if original_color == newColor:
        return image
    queue = deque([sr, sc])

    # BFS
    while queue:
        x, y = queue.popleft()
        # explore all four directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = dx + x, dy + y

            # check if new coordinates are valid and have the original color
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and \
                    image[new_x][new_y] == original_color:
                # Change the color and add the cell to the queue
                image[new_x][new_y] = newColor
                queue.append((new_x, new_y))
    return image
