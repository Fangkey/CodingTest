class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for n in nums:
            single = n ^ single

        return single



if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2, 2, 3]
    print s.singleNumber(nums)

