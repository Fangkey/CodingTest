# coding=utf-8

# 2018-05-21 16:37
# 2018-05-21 17:20

class Solution1(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        min_len = len(nums) + 1
        cur_sum = 0
        while not ((i == len(nums)) and cur_sum < s):
            if cur_sum < s:
                cur_sum += nums[i]
                i += 1
            else:
                cur_len = i - j
                if cur_len < min_len:
                    min_len = cur_len
                cur_sum -= nums[j]
                j += 1
        
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len


# 2018-05-21 18:30
# 2018-05-21 18:34

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        min_len = len(nums) + 1
        cur_sum = 0
        while j < len(nums):
            if cur_sum < s:
                cur_sum += nums[j]
                j += 1
            
            while cur_sum >= s:
                min_len = min(min_len, j - i)
                cur_sum -= nums[i]
                i += 1
                    
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len


if __name__ == "__main__":
    sl = Solution()
    
    s = 15
    nums = [1,2,3,4,5]
    # 5
    print sl.minSubArrayLen(s, nums)

    nums = [1,1]
    s = 3
    #0
    print sl.minSubArrayLen(s, nums)
    
    
    nums = [2,3,1,2,4,3]
    s = 7
    # 2
    print sl.minSubArrayLen(s, nums)