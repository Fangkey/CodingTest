# coding=utf-8

# 2018-05-21 01:31
# 2018-05-21 01:46 TLE

class Solution1(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False

        a = [x[:] for x in [[0] * len(nums)] * len(nums)]
        for i in range(0, len(nums)):
            a[i][i] = nums[i]

        for i in range(1, len(nums)):
            for j in range(0, i):
                a[j][i] = a[j][i - 1] + nums[i]
                if k == 0 and a[j][i] == 0:
                    return True
                elif k != 0 and a[j][i] % k == 0:
                    return True
        return False

# 2018-05-21 01:46 TLE
# 2018-05-21 02:01

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_set = set()

        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            if k != 0:
                cur_sum %= k
                if i != 0 and cur_sum == 0:
                    return True

            if cur_sum in mod_set:
                if k == 0 and cur_sum == 0:
                    return True
                elif k != 0:
                    return True
            else:
                mod_set.add(cur_sum)
        return False

if __name__ == "__main__":
    s = Solution()

    nums = [1, 1]
    k = 2
    # True
    print s.checkSubarraySum(nums, k)

    nums = [0, 1, 0]
    k = 0
    # False
    print s.checkSubarraySum(nums, k)

    nums = [0, 0]
    k = 0
    # True
    print s.checkSubarraySum(nums, k)

    nums = [23, 2, 6, 4, 7]
    k = 0
    # False
    print s.checkSubarraySum(nums, k)

    nums = [23, 2, 4, 6, 7]
    k = 6
    # True
    print s.checkSubarraySum(nums, k)

    nums = [23, 2, 6, 4, 7]
    k = 6
    # True
    print s.checkSubarraySum(nums, k)