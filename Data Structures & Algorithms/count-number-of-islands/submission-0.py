class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs  (r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [1,0], [-1,0], [0, -1]]
                for dr, dc in directions:
                    ROWS = row + dr
                    COLS = col + dc
                    if ROWS in range(rows) and COLS in range(cols) and grid[ROWS][COLS] == "1" and (ROWS,COLS) not in visited:
                        q.append((ROWS,COLS))
                        visited.add((ROWS,COLS))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

        