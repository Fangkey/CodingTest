class Solution(object):
    def jumpDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_step = [-1] * len(nums)

        min_step[0] = 0

        for i in range(0, len(nums)):
            n = nums[i]
            for j in range(0, n):
                if i + j + 1 < len(nums):
                    if min_step[i + j + 1] == -1 or min_step[i + j + 1] > min_step[i] + 1:
                        min_step[i + j + 1] = min_step[i] + 1

        return min_step[-1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        farthest = 0
        start = 0
        end = 0
        jump = 0
        while end < len(nums) - 1:
            jump += 1
            for i in range(start, end + 1):
                n = nums[i]
                if i + n > farthest:
                    farthest = i + n

            start = end + 1
            end = farthest
            if start > end:
                return -1

        return jump



if __name__ == "__main__":
    s = Solution()
    a = [3, 4, 3, 2, 5, 4, 3]
    # 3
    print s.jump(a)

    a = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    # 2
    print s.jump(a)

    a = [0]
    # 0
    print s.jump(a)

    a = [1]
    # 0
    print s.jump(a)

    a = [2, 3, 1, 1, 4]
    # 2
    print s.jump(a)

    a = [1, 2, 0, 1]
    # 2
    print s.jump(a)

    a = [3, 2, 1, 0, 4]
    print s.jump(a)