class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        m = [0] * n
        m[0] = 1
        m[1] = 2

        for i in range(2, n):
            m[i] = m[i - 1] + m[i - 2]

        return m[n - 1]



if __name__ == "__main__":
    s = Solution()

    print s.climbStairs(1)
    print s.climbStairs(2)
    print s.climbStairs(3)
    print s.climbStairs(5)
