# coding=utf-8

# 2018-05-17 16:05
# 2018-05-17 16:54
# 2018-05-17 16:59 revise to neat code

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        found = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                found = True
                break
            
        if not found:
             i = 0   
        else:
            for j in range(len(nums) - 1, i - 1, -1):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
        self.reverse_nums(nums, i, len(nums) - 1)
        
    def reverse_nums(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
if __name__ == "__main__":
    s = Solution()
    
    n = [3, 2, 1]
    cnt = 0
    while True:
        s.nextPermutation(n)
        print n
        cnt += 1
        if cnt == 50:
            break
        