class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        r = 1
        for i in range(m, m + n - 1):
            r = r * i
        for j in range(1, n):
            r = r / j

        return r

    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 1

        s = [x[:] for x in [[0] * n] * m]

        for i in range(0, m):
            s[i][0] = 1
        for j in range(0, n):
            s[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                s = s[i][j - 1] + s[i - 1][j]

        return s[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(1, 1)
    print s.uniquePaths(0, 0)
    print s.uniquePaths(2, 2)
    print s.uniquePaths(2, 3)

    print s.uniquePaths(1, 1)
    print s.uniquePaths(0, 0)
    print s.uniquePaths(2, 2)
    print s.uniquePaths(2, 3)