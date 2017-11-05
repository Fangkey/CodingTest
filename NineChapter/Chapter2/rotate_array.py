class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) -  1)
        self.reverse(nums, 0, len(nums) - 1)




if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 0)
    print nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 100)
    print nums