class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        visited = [0] * len(nums)
        self.helper(nums, [], visited, result)
        return result

    def helper(self, nums, cur_set, visited, result):
        if len(cur_set) == len(nums):
            result.append(cur_set[:])

        for i in range(0, len(nums)):
            if visited[i] == 1:
                continue

            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                continue

            cur_set.append(nums[i])
            visited[i] = 1
            self.helper(nums, cur_set, visited, result)
            cur_set.pop()
            visited[i] = 0


if __name__ == "__main__":
    s = Solution()
    print s.permuteUnique([1, 1, 2])