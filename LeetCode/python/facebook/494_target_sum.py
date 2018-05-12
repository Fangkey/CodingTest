# coding=utf-8

# 2018-05-13 03:54
# 2018-05-13 04:30


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        l = len(nums)
        all_sum = sum(nums)
        if S > all_sum or S < -all_sum:
            return 0

        m = [x[:] for x in [[0] * (all_sum * 2 + 1)] * (l + 1)]

        m[0][all_sum] = 1

        for i in range(0, l):
            n = nums[i]
            for j in range(0, 2 * all_sum + 1):
                if m[i][j] != 0:
                    if j + n < 2 * all_sum + 1:
                        m[i + 1][j + n] += m[i][j]
                    if j - n >= 0:
                        m[i + 1][j - n] += m[i][j]

        return m[l][all_sum + S]


if __name__ == "__main__":
    s = Solution()

    nums = [1]
    S = 2
    print s.findTargetSumWays(nums, S)


    nums = [1, 1, 1, 1, 1]
    S = 3
    print s.findTargetSumWays(nums, S)