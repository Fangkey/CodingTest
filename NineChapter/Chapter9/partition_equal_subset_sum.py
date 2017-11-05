class Solution1(object):
    def helper(self, nums, cur_index, cur_target):
        if cur_target == 0:
            return True

        if cur_target < 0:
            return False

        if cur_index > len(nums) - 1:
            return False

        found = False
        for i in range(cur_index, len(nums)):
            new_target = cur_target - nums[i]
            if self.helper(nums, i + 1, new_target):
                found = True
                break

        return found

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False

        s = s / 2

        found = self.helper(nums, 0, s)

        return found


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False

        s = s / 2

        f = [False] * (s + 1)
        f[0] = True

        for n in nums:
            for j in range(s, n - 1, -1):
                f[j] = f[j] | f[j - n]

        return f[s]

if __name__ == "__main__":
    s = Solution()

    nums = [1, 5, 11, 5]
    print s.canPartition(nums)

