class Solution:
    def dfs(self, x,y, rows, cols, visited, grid, dirs):
        cur_area = 1
        for move in dirs:
            x_new, y_new = x+move[0], y+move[1]
            if(x_new>=0 and x_new<rows and y_new>=0 and y_new < cols):
                if(grid[x_new][y_new] ==1 and not (x_new,y_new) in visited):
                    visited.add((x_new, y_new))
                    cur_area += self.dfs(x_new,y_new, rows, cols, visited,  grid, dirs)
        return cur_area

 

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None or grid[0] is None:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    if((i,j) in visited):
                        continue
                    visited.add((i,j))
                    cur_area = self.dfs(i,j,rows,cols, visited, grid, dirs)
                    if max_area < cur_area:
                        max_area = cur_area
        return max_area

        
