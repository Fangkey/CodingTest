class Solution(object):
    def findMinBetter(self, nums):
        if len(nums) == 0:
            return None

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            # 比较end，因为end永远存在，找最小，一定是右边忘左缩
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        cand_min = nums[0]
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < nums[start]:
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            temp = nums[start]
        else:
            temp = nums[end]

        if cand_min < temp:
            return cand_min
        else:
            return temp



if __name__ == "__main__":
    s = Solution()
    print s.findMinBetter([4, 5, 6, 7, 0, 1, 2])
    print s.findMinBetter([0, 1, 2, 3, 4, 5, 6])