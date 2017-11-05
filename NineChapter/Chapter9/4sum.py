class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = set()
        for i in range(0, len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums [j]

                sum = target - a - b
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    ns = nums[start]
                    ne = nums[end]
                    if ns + ne > sum:
                        end -= 1
                    elif ns + ne < sum:
                        start += 1
                    else:
                        s = [a, b, ns, ne]
                        s = sorted(s)
                        result.add(tuple(s))
                        start += 1
                        end -= 1

        return list(result)


if __name__ == "__main__":
    s = Solution()

    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print s.fourSum(nums, target)