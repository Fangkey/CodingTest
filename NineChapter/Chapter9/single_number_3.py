class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        for n in nums:
            sum = sum ^ n

        cnt = 0
        while sum != 0:
            if sum >> cnt & 1 != 0:
                break
            cnt += 1

        sum0 = 0
        sum1 = 0
        for n in nums:
            if (n >> cnt & 1) == 1:
                sum1 = sum1 ^ n
            else:
                sum0 = sum0 ^ n

        return [sum0, sum1]


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 1, 3, 2, 5]
    # [3, 5]
    print s.singleNumber(nums)


