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

if __name__ == "__main__":
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]

    print s.longestConsecutive(nums)