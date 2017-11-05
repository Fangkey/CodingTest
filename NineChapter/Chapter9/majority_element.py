class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_n = nums[0]
        cur_cnt = 1

        for n in nums[1:]:
            if cur_cnt == 0:
                cur_cnt = 1
                cur_n = n
            else:
                if n == cur_n:
                    cur_cnt += 1
                else:
                    cur_cnt -= 1

        return cur_n


if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 1, 1, 2, 2, 2]
    print s.majorityElement(nums)