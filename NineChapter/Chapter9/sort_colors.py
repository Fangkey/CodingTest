class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s = 0
        e = len(nums) - 1
        while s < e:
            if nums[s] == 0:
                s += 1
            elif nums[e] == 0:
                t = nums[s]
                nums[s] = nums[e]
                nums[e] = t
                s += 1
                e -= 1
            else:
                e -= 1

        e = len(nums) - 1
        while s < e:
            if nums[s] > nums[e]:
                t = nums[s]
                nums[s] = nums[e]
                nums[e] = t
                s += 1
                e -= 1
            elif nums[e] == 2:
                e -= 1
            else:
                s += 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 2, 0, 1, 2, 0, 0, 0, 2, 2, 2, 1, 1, 1]
    s.sortColors(nums)
    print nums