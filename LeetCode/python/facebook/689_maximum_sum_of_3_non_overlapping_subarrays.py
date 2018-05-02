# coding=utf-8

# 2018-05-01 20:16
# 2018-05-01 21：02 time exceeded

class Solution1(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)

        sub_sum = []
        cur_sum = sum(nums[0: k])
        sub_sum.append(cur_sum)
        for i in range(1, l - k + 1):
            cur_sum = cur_sum - nums[i - 1] + nums[i + k - 1]
            sub_sum.append(cur_sum)

        a = [x[:] for x in [[[0, 0]] * l] * l]
        for i in range(0, l):
            for j in range(i + k - 1, l):
                if j - i + 1 < k or j == 0:
                    continue
                s = sub_sum[j - k + 1]
                if s > a[i][j - 1][0]:
                    a[i][j] = [s, j - k + 1]
                else:
                    a[i][j] = a[i][j - 1]

        max_sum = 0
        d_list = []
        for d1 in range(0, l - 2 * k):
            for d2 in range(d1 + 1, l - k):
                cur_max = a[0][d1][0] + a[d1 + 1][d2][0] + a[d2 + 1][l - 1][0]
                if cur_max > max_sum:
                    max_sum = cur_max
                    d_list = [a[0][d1], a[d1 + 1][d2], a[d2 + 1][l - 1]]

        return [d_list[0][1], d_list[1][1], d_list[2][1]]



# 2018-05-01 21：02
# 2018-05-01 22:15

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)

        sub_sum = []
        cur_sum = sum(nums[0: k])
        sub_sum.append(cur_sum)
        for i in range(1, l - k + 1):
            cur_sum = cur_sum - nums[i - 1] + nums[i + k - 1]
            sub_sum.append(cur_sum)

        left = [[0, 0]] * l
        for i in range(k - 1, l - k + 1):
            if sub_sum[i - k + 1] > left[i - 1][0]:
                left[i] = [sub_sum[i - k + 1], i - k + 1]
            else:
                left[i] = left[i - 1]

        right = [[sub_sum[l-k], l - k]] * l
        for i in range(l - k, 0, -1):
            if sub_sum[i - 1] >= right[i][0]:
                right[i - 1] = [sub_sum[i - 1], i - 1]
            else:
                right[i - 1] = right[i]

        max_sum = 0
        result = []
        for j in range(k, l - 2 * k + 1):
            cur_sum = left[j - 1][0] + sub_sum[j] + right[j + k][0]
            if cur_sum > max_sum:
                max_sum = cur_sum
                result = [left[j - 1][1], j, right[j + k][1]]

        return result

if __name__ == "__main__":
    s = Solution()
    # [4, 5, 7]
    print s.maxSumOfThreeSubarrays([4, 5, 10, 6, 11, 17, 4, 11, 1, 3], 1)
    # [1, 4, 7]
    print s.maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3)
    # [0, 3, 5]
    print s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)