from typing import List


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    rows, cols = len(grid), len(grid[0])

    if not grid:
        return count

    # Make the current island visited by marking it as '0'
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark as visited
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Visit all islands and count them
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':  # Found an island
                count += 1
                dfs(i, j)  # Mark the entire island as visited

    return count

grid = [
    ['0','1','1','0','1'],
    ['1','0','1','0','1'],
    ['0','1','1','0','1'],
    ['0','1','0','0','1']
    ]
 
print(numIslands(grid)) # Output: 3