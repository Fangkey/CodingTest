import sys

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = sys.maxint
        for n in nums:
            if n < minimum:
                minimum = n
        return minimum


if __name__ == "__main__":
    s = Solution()
    print s.findMin([4, 5, 6, 7, 0, 1, 2])
    print s.findMin([0, 1, 2, 3, 4, 5, 6])