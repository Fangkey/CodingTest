import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff = sys.maxint
        for i, n in enumerate(nums):
            sum = target - n
            start = i + 1
            end = len(nums) - 1
            while start < end:
                ns = nums[start]
                ne = nums[end]
                diff = abs(ns + ne - sum)
                if diff < min_diff:
                    min_diff = diff
                    solution = [n, ns, ne]
                if ns + ne > sum:
                    end -= 1
                elif ns + ne < sum:
                    start += 1
                else:
                    return n + ns + ne

        return solution[0] + solution[1] + solution[2]


if __name__ == "__main__":
    s = Solution()

    nums = [0,1,2]
    # 3
    print s.threeSumClosest(nums, 0)

    nums = [-1, 2, 1, -4]
    # 2
    print s.threeSumClosest(nums, 2)