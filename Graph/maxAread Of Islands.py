def maxAreaOfIsland(grid: List[List[int]]) -> int:
    max_area = 0
    row, column = len(grid), len(grid[0])
    if not grid:
        return max_area
    

    def dfs(r, c):
        if r < 0 or r >= row or c < 0 or c >= column or grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0
        a1 = dfs(r-1, c)
        a2 = dfs(r+1, c)
        a3 = dfs(r, c-1)
        a4 = dfs(r, c+1)

        # 1 is for current cell area
        # a1, a2, a3, a4 are for the area of 4 directions
        return 1 + a1+a2+a3+a4
    
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                # Find the max area
                max_area = max(max_area, dfs(i, j))

    return max_area





grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(maxAreaOfIsland(grid)) # Output: 5