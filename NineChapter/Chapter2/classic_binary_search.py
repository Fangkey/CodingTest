class Solution(object):
    def findPosition(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                return mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end

        return -1

if __name__ == "__main__":
    s = Solution()
    print s.findPosition([], 10)
    print s.findPosition([1, 2, 3, 4, 5, 6, 7], 4)
    print s.findPosition([1, 2, 3, 5, 6, 7], 4)