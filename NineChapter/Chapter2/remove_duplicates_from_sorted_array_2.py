# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 记下来，必须有状态，否则无法区分是该移动一位还是两位
        if len(nums) == 0:
            return 0

        size = 0
        cur = 0
        count = 0
        while cur < len(nums) - 1:
            if nums[cur + 1] != nums[size]:
                cur += 1
                size += 1
                nums[size] = nums[cur]
                count = 0
            else:
                if count < 1:
                    count += 1
                    size += 1
                    nums[size] = nums[cur + 1]
                cur += 1
        return size + 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 1, 3, 3]
    print s.removeDuplicates(nums)
    print nums

    nums = [1,1,2]
    print s.removeDuplicates(nums)
    print nums

    nums = [0, 1, 2, 3, 4, 5, 6]
    print s.removeDuplicates(nums)
    print nums

    nums = [0, 1, 1, 3, 4, 4, 5, 6, 6, 7]
    print s.removeDuplicates(nums)
    print nums

    nums = [0, 1, 1, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7]
    print s.removeDuplicates(nums)
    print nums