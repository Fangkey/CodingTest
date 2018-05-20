# coding=utf-8

# 2018-05-21 00:58
# 2018-05-21 01:15

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        res = []
        res.append(nums[0])
        for i in range(1, len(nums)):
            res.append(res[i - 1] * nums[i])

        right = 1
        for i in range(len(nums) - 1, 0, -1):
            res[i] = res[i - 1] * right
            right *= nums[i]
        res[0] = right
        return res


if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3,4]
    print s.productExceptSelf(nums)