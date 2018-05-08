# coding=utf-8
#2018-05-03 01:36
#2018-05-03 01:47

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        power = 1
        remain = abs(n)
        if n < 0:
            x = 1 / x
        while remain > 0:
            t = 1
            p = x
            while t * 2 < remain:
                p *= p
                t *= 2
            remain -= t
            power *= p

        return power

if __name__ == "__main__":
    s = Solution()
    x = 2.0
    n = -2
    print s.myPow(x, n)

    x = 2.0
    n = 3
    print s.myPow(x, n)