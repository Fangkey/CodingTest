class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, n in enumerate(nums):
            d[n] = i

        for i, n in enumerate(nums):
            if target - n in d:
                if d[target - n] != i:
                    return [i, d[target - n]]


if __name__ == "__main__":
    s = Solution()

    nums = [3,3]
    target = 6
    print s.twoSum(nums, target)