# coding=utf-8

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for n in nums:
            d[n] = False

        longest = 0
        for n in nums:
            if d[n] is True:
                continue

            d[n] = True

            down = n - 1
            while down in d:
                d[down] = True
                down -= 1

            up = n + 1
            while up in d:
                d[up] = True
                up += 1

            length = up - down - 1

            if length > longest:
                longest = length

        return longest


# 2018-05-13 01:25
# 2018-05-13 01:37

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}

        for n in nums:
            nums_dict[n] = 0

        max_cnt = 0
        for n in nums:
            if nums_dict[n] != 0:
                continue

            cnt = 0
            cur = n
            while cur in nums_dict and nums_dict[cur] == 0:
                nums_dict[cur] = 1
                cur += 1
                cnt +=1

            cur = n - 1
            while cur in nums_dict and nums_dict[cur] == 0:
                nums_dict[cur] = 1
                cur -= 1
                cnt += 1

            if cnt > max_cnt:
                max_cnt = cnt

        return max_cnt

if __name__ == "__main__":
    s = Solution()
    # 4
    nums = [100, 4, 200, 1, 3, 2]

    print s.longestConsecutive(nums)