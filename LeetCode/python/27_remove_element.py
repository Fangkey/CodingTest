# coding=utf-8

# 2018-05-16 14:57
# 2018-05-16 15:17

class Solution1(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        i = 0
        j = 0
        
        while i < len(nums) and nums[i] != val:
            i += 1
        
        while j < len(nums):
            if nums[j] == val:
                break
            j += 1
        
        while j < len(nums):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        
        return i
    
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
    
if __name__ == "__main__":
    s = Solution()
    
    nums = [2]
    val = 3
    print s.removeElement(nums, val)
    print nums
    
    nums = []
    val = 0
    print s.removeElement(nums, val)
    print nums
    
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print s.removeElement(nums, val)
    print nums
    
    
    nums = [3,2,2,3]
    val = 3
    print s.removeElement(nums, val)
    print nums
    
    
    