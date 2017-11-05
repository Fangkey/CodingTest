class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        start = 0
        end = len(nums) - 1

        # search for left boundary
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                end = mid
            elif target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid


        if nums[start] == target:
            left_boundary = start
        elif nums[end] == target:
            left_boundary = end
        else:
            return [-1, -1]

        start = left_boundary
        end = len(nums) - 1
        # search for right boundary
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid

        if nums[end] == target:
            right_boundary = end
        elif nums[start] == target:
            right_boundary = start

        return [left_boundary, right_boundary]


if __name__ == "__main__":
    s = Solution()
    print s.searchRange([], 10)
    print s.searchRange([2, 2], 2)
    print s.searchRange([1, 2, 2, 2, 2, 4, 5, 6, 7], 2)
    print s.searchRange([1, 2, 2, 2, 2, 4, 5, 6, 7], 4)
    print s.searchRange([1, 2, 3, 5, 6, 7], 4)