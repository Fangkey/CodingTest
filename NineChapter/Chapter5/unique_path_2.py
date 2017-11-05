class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 1
        n = len(obstacleGrid[0])
        if n == 0:
            return 1

        s = [x[:] for x in [[0] * n] * m]

        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                break
            s[i][0] = 1

        for j in range(0, n):
            if obstacleGrid[0][j] == 1:
                break
            s[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    s[i][j] = 0
                else:
                    s[i][j] = s[i - 1][j] + s[i][j-1]

        return s[-1][-1]


if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    print s.uniquePathsWithObstacles(obstacleGrid)