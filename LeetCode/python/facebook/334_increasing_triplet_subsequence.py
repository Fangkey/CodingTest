# coding=utf-8

# 2018-05-26 15:05
# 2018-05-26 16:03
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        first_min = sys.maxint
        second_min = sys.maxint
        
        for n in nums:
            if n <= first_min:
                first_min = n
            elif n <= second_min:
                second_min = n
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    
    nums = [1, 2, 3, 4, 5]
    print s.increasingTriplet(nums)
    
    nums = [5, 4, 3, 2, 1]
    print s.increasingTriplet(nums)