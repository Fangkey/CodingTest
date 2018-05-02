#coding=utf-8
#2018-05-03 01:15
#2018-05-03 01:34

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        h = len(grid)
        w = len(grid[0])
        visited = [x[:] for x in [[0] * w] * h]

        count = 0
        for i in range(0, h):
            for j in range(0, w):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    self.visit_grid(grid, h, w, i, j, visited)
                    count += 1

        return count

    def visit_grid(self, grid, h, w, i, j, visited):
        visited[i][j] = 1
        # left
        if i > 0:
            if grid[i - 1][j] == "1" and visited[i - 1][j] == 0:
                self.visit_grid(grid, h, w, i - 1, j, visited)

        # right
        if i < h - 1:
            if grid[i + 1][j] == "1" and visited[i + 1][j] == 0:
                self.visit_grid(grid, h, w, i + 1, j, visited)
        # up
        if j > 0:
            if grid[i][j - 1] == "1" and visited[i][j - 1] == 0:
                self.visit_grid(grid, h, w, i, j - 1, visited)
        # down
        if j < w - 1:
            if grid[i][j + 1] == "1" and visited[i][j + 1] == 0:
                self.visit_grid(grid, h, w, i, j + 1, visited)


if __name__ == "__main__":
    s = Solution()

    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    # 1
    print s.numIslands(grid)

    grid = [
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    # 2
    print s.numIslands(grid)

    grid = [
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    # 3
    print s.numIslands(grid)