class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 黑盒测试，如果只有一个数不同，之前不会得到任何信息消除掉大量信息
        for i, n in enumerate(nums):
            if n == target:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print s.search([4, 5, 6, 7, 0, 1, 2], 4)
    print s.search([4, 5, 6, 7, 0, 1, 2], 3)
