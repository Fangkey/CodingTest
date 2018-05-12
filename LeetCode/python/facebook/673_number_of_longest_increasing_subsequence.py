# coding=utf-8

# 2018-05-13 04:34
# 2018-05-13 04:22

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        l = len(nums)
        m = [[0, 0]] * (l + 1)
        m[1] = [1, 1]

        for i in range(1, l):
            cur = nums[i]
            cur_max = 0
            max_cnt = 1
            for j in range(0, i):
                if nums[j] < cur:
                    if m[j + 1][0] > cur_max:
                        cur_max = m[j + 1][0]
                        max_cnt = m[j + 1][1]
                    elif m[j + 1][0] == cur_max:
                        max_cnt += m[j + 1][1]

            m[i + 1] = [cur_max + 1, max_cnt]

        max_len = max([i[0] for i in m])
        cnt = 0
        for i in m:
            if i [0] == max_len:
                cnt += i[1]
        return cnt


if __name__ == "__main__":
    s = Solution()

    nums = [1,2,4,3,5,4,7,2]
    print s.findNumberOfLIS(nums)

    nums = [2,2,2,2,2]
    print s.findNumberOfLIS(nums)

    nums = [1,3,5,4,7]
    print s.findNumberOfLIS(nums)