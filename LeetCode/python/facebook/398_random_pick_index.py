# coding=utf-8

# 2018-05-21 02:07
# 2018-05-21 02:35 Reservoir Sampling

import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        selected_i = -1
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                if random.randint(1, count) == 1:
                    selected_i = i
        return selected_i


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

if __name__ == "__main__":

    nums = [1, 2, 3, 3, 3]

    s = Solution(nums)
    print s.pick(1)
    print s.pick(2)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)
    print s.pick(3)