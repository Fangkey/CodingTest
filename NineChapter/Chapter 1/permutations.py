class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        set_has = set()
        self.helper(nums, [], set_has, result)
        return result

    def helper(self, nums, cur_set, set_has, result):
        if len(cur_set) == len(nums):
            result.append(cur_set[:])
            return

        for i in range(0, len(nums)):
            cur_num = nums[i]
            if cur_num in set_has:
                continue
            cur_set.append(cur_num)
            set_has.add(cur_num)
            self.helper(nums, cur_set, set_has, result)
            cur_set.pop()
            set_has.discard(cur_num)



if __name__ == "__main__":
    s = Solution()
    print s.permute([1, 2, 3])