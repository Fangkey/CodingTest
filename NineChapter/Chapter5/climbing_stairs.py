# coidng=utf-8

class Solution1(object):
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


# 2018-05-10 22:47
# 2018-05-10 22:50

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n + 1)
        a[0] = 1
        a[1] = 1
        for i in range(2, n + 1):
            a[i] = a[i - 1] + a[i - 2]

        return a[-1]

if __name__ == "__main__":
    s = Solution()

    # 1
    print s.climbStairs(1)
    # 2
    print s.climbStairs(2)
    # 3
    print s.climbStairs(3)
    # 8
    print s.climbStairs(5)
