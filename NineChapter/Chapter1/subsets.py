class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, [], 0, result)
        return result

    def helper(self, nums, cur_set, cur_index, result):
        result.append(cur_set[:])
        for i in range(cur_index, len(nums)):
            cur_set.append(nums[i])
            self.helper(nums, cur_set, i + 1, result)
            cur_set.pop()


if __name__ == "__main__":
    s = Solution()
    print s.subsets([1, 2, 3])