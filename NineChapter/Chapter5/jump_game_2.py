# coding=utf-8
class Solution1(object):
    def jumpDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_step = [-1] * len(nums)

        min_step[0] = 0

        for i in range(0, len(nums)):
            n = nums[i]
            for j in range(0, n):
                if i + j + 1 < len(nums):
                    if min_step[i + j + 1] == -1 or min_step[i + j + 1] > min_step[i] + 1:
                        min_step[i + j + 1] = min_step[i] + 1

        return min_step[-1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        farthest = 0
        start = 0
        end = 0
        jump = 0
        while end < len(nums) - 1:
            jump += 1
            for i in range(start, end + 1):
                n = nums[i]
                if i + n > farthest:
                    farthest = i + n

            start = end + 1
            end = farthest
            if start > end:
                return -1

        return jump


# 2018-05-10 23:50
# 2018-05-10 23:57 DP time exceeded
# 2018-05-11 00:25 Greedy

class Solution(object):
    def jumpDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        a = [sys.maxint] * (len(nums) + 1)
        a[0] = 0
        a[1] = 0
        for i in range(1, len(nums) + 1):
            step = nums[i - 1]
            for j in range(i + 1, min(len(nums) + 1, i + step + 1)):
                if a[j] > a[i] + 1:
                    a[j] = a[i] + 1
        return a[-1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or len(nums) == 0:
            return 0

        step = 1
        start = 0
        end = nums[0]
        furthest = end
        while end < len(nums) - 1:
            for i in range(start, end + 1):
                if i + nums[i] > furthest:
                    furthest = i + nums[i]
            step += 1
            start = end + 1
            end = furthest
            if start > end:
                return -1

        return step


if __name__ == "__main__":
    s = Solution()
    a = [3, 4, 3, 2, 5, 4, 3]
    # 3
    print s.jump(a)

    a = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    # 2
    print s.jump(a)

    a = [0]
    # 0
    print s.jump(a)

    a = [1]
    # 0
    print s.jump(a)

    a = [2, 3, 1, 1, 4]
    # 2
    print s.jump(a)

    a = [1, 2, 0, 1]
    # 2
    print s.jump(a)

    a = [3, 2, 1, 0, 4]
    print s.jump(a)