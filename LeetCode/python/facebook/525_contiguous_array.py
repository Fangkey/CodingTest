# coding=utf-8

# 2018-06-01 19:01
# 2018-06-01 19:06

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_dict = dict()
        cnt = 0
        max_len = 0
        cnt_dict[0] = -1
        for i, n in enumerate(nums):
            if n == 0:
                cnt += 1
            else:
                cnt -=1
            if cnt in cnt_dict:
                if i - cnt_dict[cnt] > max_len:
                    max_len = i - cnt_dict[cnt]
            else:
                cnt_dict[cnt] = i
                
        return max_len

if __name__ == "__main__":
    s = Solution()
    
    nums = [0]
    print s.findMaxLength(nums)
    
    nums = [0,1,0]
    print s.findMaxLength(nums)
    
    nums = [0,1]
    print s.findMaxLength(nums)
    
                