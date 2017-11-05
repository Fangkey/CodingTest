import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        sum = 0
        # important
        acc_array = [0]
        for n in nums:
            sum += n
            acc_array.append(sum)

        cur_min = acc_array[0]
        max_diff = -sys.maxint
        left = right = cur_left = 0
        for i in range(1, len(acc_array)):
            s = acc_array[i]
            if s - cur_min > max_diff:
                max_diff = s - cur_min
                right = i
                left = cur_left
            if s < cur_min:
                cur_min = s
                cur_left = i

        return max_diff


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2]
    # 3
    print s.maxSubArray(nums)

    nums = []
    # 0
    print s.maxSubArray(nums)

    nums = [-1]
    # -1
    print s.maxSubArray(nums)

    nums = [1]
    # 1
    print s.maxSubArray(nums)

    nums = [1, -1]
    # 1
    print s.maxSubArray(nums)

    nums = [-1, -1]
    # -1
    print s.maxSubArray(nums)

    nums = [-1, 1]
    # 1
    print s.maxSubArray(nums)

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # [4, -1, 2, 1]
    # 6
    print s.maxSubArray(nums)