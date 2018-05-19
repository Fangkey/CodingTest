# coding=utf-8

# 2018-05-18 16:41

# 2018-05-19 20:50
# 2018-05-19 21:01
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        
        for i in range(0, len(nums)):
            next_i = nums[i]
            if next_i - 1 != i:
                while next_i - 1 >= 0 and next_i - 1 < len(nums) and next_i != nums[next_i - 1]:
                    n = nums[next_i - 1]
                    nums[next_i - 1] = next_i
                    next_i = n
                    
        for i, n in enumerate(nums):
            if i != n - 1:
                return i + 1
            
        return len(nums) + 1

if __name__ == "__main__":
    s = Solution()
    
    nums = [1]
    # 2
    print s.firstMissingPositive(nums)
    
    nums = []
    # 1
    print s.firstMissingPositive(nums)
    
    nums = [3,4,-1,1]
    # 2
    print s.firstMissingPositive(nums)
    
    nums = [1,2,0]
    # 3
    print s.firstMissingPositive(nums)

    # 1
    nums = [7,8,9,11,12]
    print s.firstMissingPositive(nums)