class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        elif target < nums[start]:
            return 0
        elif target > nums[end]:
            return len(nums)
        else:
            return end

if __name__ == "__main__":
    s = Solution()
    print s.searchInsert([], 10)
    print s.searchInsert([1, 2], 2)
    print s.searchInsert([1, 2, 4, 5, 6, 7], 3)
    print s.searchInsert([1, 2, 3, 4, 5, 6, 7], 8)
    print s.searchInsert([1, 2, 3, 5, 6, 7], 0)