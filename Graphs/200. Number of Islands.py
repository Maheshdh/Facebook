class Solution:
    def dfs(self,x,y,seen,dirs,rows,cols,grid):
        for move in dirs:
            x_new, y_new = x + move[0], y+move[1]
            if x_new >= 0 and x_new < rows and y_new >=0 and y_new < cols:
                if(grid[x_new][y_new]=="1" and not (x_new,y_new) in seen):
                    seen.add((x_new,y_new))
                    self.dfs(x_new,y_new,seen,dirs,rows,cols,grid)


        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        result = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1"):
                    if ((i,j) in seen):
                        continue
                    else:
                        seen.add((i,j))
                        result += 1
                        self.dfs(i,j,seen,dirs,rows,cols,grid)
        return result
