
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = []
        for i in range(0, len(grid)):
            l = grid[i]
            lm = []
            for j in range(0, len(l)):
                n = l[j]
                if i == 0 and j == 0:
                    lm.append(l[j])
                elif i == 0:
                    lm.append(lm[j - 1] + l[j])
                elif j == 0:
                    lm.append(m[i - 1][j] + l[j])
                else:
                    lm.append(min(m[i - 1][j], lm[j - 1]) + l[j])
            m.append(lm)

        return m[-1][-1]

    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # Important
        s = [x[:] for x in [[0] * n] * m]
        s[0][0] = grid[0][0]

        for i in range(1, m):
            s[i][0] = s[i - 1][0] + grid[i][0]

        for j in range(1, n):
            s[0][j] = s[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                s[i][j] = min(s[i - 1][j], s[i][j - 1]) + grid[i][j]

        return s[-1][-1]


if __name__ == "__main__":
    s = Solution()

    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print s.minPathSum2(grid)

    grid = [
        [1,2,5],
        [3,2,1]
    ]
    print s.minPathSum2(grid)

    grid = [
        [1, 1],
        [2, 1]
    ]

    print s.minPathSum2(grid)