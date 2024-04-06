class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = []
                    moves = self.dfs(i,j,grid,"O",path)
                    islands.add("".join(path))
        return len(islands)
    
    def dfs(self,x,y,grid,move,path):
        if x>=0 and x < len(grid) and y>=0 and y < len(grid[0]) and grid[x][y] == 1:
            grid[x][y] = 0 
            path.append(move)
            self.dfs(x+1,y,grid,"S",path)
            self.dfs(x,y-1,grid,"W",path)
            self.dfs(x-1,y,grid,"N",path)
            self.dfs(x,y+1,grid,"E",path)
            path.append("B")
            

        
