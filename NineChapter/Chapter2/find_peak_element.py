class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid == 0 or nums[mid - 1] < nums[mid]:
                start = mid
            elif mid == len(nums) - 1 or nums[mid + 1] < nums[mid]:
                end = mid
            else:
                # important!
                start = mid

        if nums[start] > nums[end]:
            return start
        else:
            return end


if __name__ == "__main__":
    s = Solution()
    print s.findPeakElement([2, 1, 2])
    print s.findPeakElement([1, 2, 3, 1])
    print s.findPeakElement([1, 2, 3, 2, 1])
    print s.findPeakElement([1, -1, -2, -3])
    print s.findPeakElement([-3, -2, -1, 1])
