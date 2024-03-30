class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        q = deque()
        q.append((0,0,1))
        visited = set()
        visited.add((0,0))
        n = len(grid)
        moves = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
        while q:
            front = q.popleft()
            row, col, length = front
            if row == n-1 and col == n-1:
                return length
            for move in moves:
                row_new,col_new = row + move[0], col + move[1]
                if row_new >= 0 and col_new >=0 and row_new < n and col_new < n and grid[row][col] == 0 and not (row_new,col_new) in visited:
                    visited.add((row_new,col_new))
                    q.append((row_new,col_new,length+1))
        return -1
            

        
