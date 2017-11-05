class Solution(object):
    def search(self, nums, target):
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
            if nums[mid] >= nums[start]:
                if target >= nums[start]:
                    if nums[mid] > target:
                        end = mid
                    elif nums[mid] < target:
                        start = mid
                    else:
                        return mid
                elif target < nums[start]:
                    start = mid
                else:
                    return start
            elif nums[mid] < nums[start]:
                if target >= nums[start]:
                    end = mid
                elif target < nums[start]:
                    if nums[mid] > target:
                        end = mid
                    elif nums[mid] < target:
                        start = mid
                    else:
                        return mid
                else:
                    return start

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1



if __name__ == "__main__":
    s = Solution()
    print s.search([4, 5, 6, 7, 0, 1, 2], 4)
    print s.search([4, 5, 6, 7, 0, 1, 2], 6)
    print s.search([4, 5, 6, 7, 0, 1, 2], 7)
    print s.search([4, 5, 6, 7, 0, 1, 2], 0)
    print s.search([4, 5, 6, 7, 0, 1, 2], 2)
    print s.search([4, 5, 6, 7, 0, 1, 2], 3)
    print s.search([4, 5, 6, 7, 0, 1, 2], 8)

