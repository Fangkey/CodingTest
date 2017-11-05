# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version == 5:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start + 1 < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid

        if isBadVersion(start):
            return start
        elif isBadVersion(end):
            return end
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    print s.firstBadVersion(10)
    print s.firstBadVersion(5)
    print s.firstBadVersion(4)
    print s.firstBadVersion(1)
    print s.firstBadVersion(0)