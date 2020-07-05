class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i, j):
            grid[i][j] = '0'
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in dirs:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count