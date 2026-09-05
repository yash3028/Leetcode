from collections import deque


class Solution:
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        # entrance
        er, ec = entrance
        # store row, col, steps
        q = deque([(er, ec, 0)])
        # entrance is visited we cant exit through entrance
        maze[er][ec] = "+"
        while q:
            # next cell to explore
            r, c, steps = q.popleft()
            # if end of row or start or row and column not the entrance then return steps
            if (r, c) != (er, ec) and (
                r == 0 or r == rows - 1 or c == 0 or c == cols - 1
            ):
                return steps
            # checking all directions 
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                # if cell is empty we found way to exit
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    maze[nr][nc] = "+"
                    q.append((nr, nc, steps + 1))
        return -1

ans = Solution().nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2])
print(ans)