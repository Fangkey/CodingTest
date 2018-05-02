# coding=utf-8
# 2018-04-30 15:32
# 2018-04-30 16:01

# hard! tricky!

class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        finish = False
        while True :
            for index in range(i, len(nums)):
                if nums[index] == 0:
                    i = index
                    break
                elif index == len(nums) - 1:
                    finish = True

            for index in range(i, len(nums)):
                if nums[index] != 0:
                    j = index
                    break
                elif index == len(nums) - 1:
                    finish = True

            if finish:
                break

            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_non_zero_pos = 0
        cur_pos = 0

        while cur_pos < len(nums):
            if nums[cur_pos] != 0:
                nums[cur_pos], nums[last_non_zero_pos] = nums[last_non_zero_pos], nums[cur_pos]
                last_non_zero_pos += 1
            cur_pos += 1

if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 0, 0, 1]
    s.moveZeroes(nums)
    print nums

    nums = [1, 0, 1]
    s.moveZeroes(nums)
    print nums

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print nums

    nums = [0, 0, 0, 0, 0]
    s.moveZeroes(nums)
    print nums

    nums = [1, 2, 3, 4, 5]
    s.moveZeroes(nums)
    print nums

    nums = [1, 2, 3, 0, 0]
    s.moveZeroes(nums)
    print nums