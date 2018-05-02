class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        self.helper(nums, [], 0, result)
        return result

    def helper(self, nums, cur_set, cur_index, result):
        result.append(cur_set[:])
        for i in range(cur_index, len(nums)):
            if i > cur_index and nums[i] == nums[i - 1]:
                continue
            cur_set.append(nums[i])
            self.helper(nums, cur_set, i + 1, result)
            cur_set.pop()


if __name__ == "__main__":
    s = Solution()
    print s.subsetsWithDup([1, 2, 2])