# coding=utf-8

# 2018-05-21 01:18
# 2018-05-21 01:29

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        bins = []
        for n in nums:
            bins.append(str(bin(n))[2:])

        max_len = max([len(b) for b in bins])

        cnt = len(nums)
        hamming = 0
        for i in range(0, max_len):
            one_cnt = 0
            for b in bins:
                b= b.zfill(max_len)
                if b[i] == "1":
                    one_cnt += 1
            hamming += one_cnt * (cnt - one_cnt)

        return hamming


if __name__ == "__main__":
    s = Solution()

    nums = [4, 14, 2]
    print s.totalHammingDistance(nums)