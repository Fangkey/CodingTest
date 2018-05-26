# coding=utf-8

# 2018-05-26 13:17                    
# 2018-05-26 14:10 TLE                
class Solution1(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = []
        self.helper(nums, [], target, result)
        return len(result)
        
    def helper(self, nums, cur_set, t_remain, result):
        if t_remain == 0:
            result.append(cur_set[:])
            return
        
        for i in range(0, len(nums)):
            n = nums[i]
            if t_remain - n >= 0:
                cur_set.append(n)
                self.helper(nums, cur_set, t_remain - n, result)
                cur_set.pop()
                       
# 2018-05-26 14:34
# 2018-05-26 14:38
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        a = [0] * (target + 1)
        a[0] = 1
        
        for i in range(1, target + 1):
            for n in nums:
                if n > i:
                    break
                if n == i:
                    a[i] += 1
                if n < i:
                    a[i] += a[i - n]
        return a[target]
                       
if __name__ == "__main__":
    s = Solution()
    
    nums = [1, 2, 3]
    target = 4
    print s.combinationSum4(nums, target)