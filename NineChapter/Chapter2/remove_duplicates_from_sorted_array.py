# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 记下来
        if len(nums) == 0:
            return 0

        size = 0
        cur = 0
        while cur < len(nums) - 1:
            if nums[size] != nums[cur + 1]:
                size += 1
                cur += 1
                nums[size] = nums[cur]
            else:
                cur += 1

        return size + 1


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    print s.removeDuplicates(nums)
    print nums

    nums = [0, 1, 2, 3, 4, 5, 6]
    print s.removeDuplicates(nums)
    print nums

    nums = [0, 1, 1, 3, 4, 4, 5, 6, 6, 7]
    print s.removeDuplicates(nums)
    print nums