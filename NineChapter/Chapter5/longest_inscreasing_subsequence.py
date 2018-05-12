# coding=utf-8
class SolutionDP(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        f = [1] * (len(nums))

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if f[j] + 1 > f[i]:
                        f[i] = f[j] + 1

        return max(f)


# important
import sys
class Solution(object):
    def binarySearch(self, l, num):
        start = 0
        end = len(l) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if l[mid] < num:
                start = mid
            elif l[mid] > num:
                end = mid
            else:
                break

        if l[mid] == num:
            return mid + 1

        if l[end] > num:
            return end

        if l[end] == num:
            return end + 1


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        f = [sys.maxint] * (len(nums) + 1)
        f[0] = -sys.maxint

        for n in nums:
            index = self.binarySearch(f, n)
            f[index] = n

        for i in range(len(nums) - 1, 0, -1):
            if f[i] != sys.maxint:
                return i


# 2018-05-13 01:38
# 2018-05-13 02:03

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        a = [1] * len(nums)
        for i in range(1, len(nums)):
            cur = nums[i]
            for j in range(i - 1, -1, -1):
                if nums[j] < cur:
                    if a[j] + 1 > a[i]:
                        a[i] = a[j] + 1
        return max(a)


if __name__ == "__main__":
    s = Solution()

    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    # 6
    print s.lengthOfLIS(nums)

    nums = [2, 2]
    # 1
    print s.lengthOfLIS(nums)

    nums = []
    # 0
    print s.lengthOfLIS(nums)

    nums = [10, 9, 2, 5, 3, 4]
    # 3
    print s.lengthOfLIS(nums)

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # 4
    print s.lengthOfLIS(nums)