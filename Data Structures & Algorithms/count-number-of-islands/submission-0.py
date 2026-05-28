class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, isNew):
            nonlocal numIslands
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == '0' or
                (r, c) in visited
            ): return

            if isNew:
                numIslands += 1

            visited.add((r,c))
            dfs(r + 1, c, False)
            dfs(r - 1, c, False)
            dfs(r, c + 1, False)
            dfs(r, c - 1, False)

            return
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, True)

        return numIslands

        