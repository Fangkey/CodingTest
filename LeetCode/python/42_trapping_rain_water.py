# coding=utf-8

# 2018-05-20 2:00
# 2018-05-20 2:30 Two direction

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v = 0
        cur_max = 0
        cur_max_i = 0
        for i in range(0, len(height)):
            if height[i] >= cur_max:
                # calc from cur_max_i to i
                for j in range(cur_max_i, i):
                    v += (cur_max - height[j])
                cur_max = height[i]
                cur_max_i = i

        left_max = 0
        left_max_i = len(height) - 1
        for i in range(len(height) - 1, cur_max_i - 1, -1):
            if height[i] >= left_max:
                # calc from left_max_i, to i
                for j in range(left_max_i, i, -1):
                    v += (left_max - height[j])
                left_max = height[i]
                left_max_i = i

        return v

if __name__ == "__main__":
    s = Solution()
    # 2
    height = [2,0,2]
    #
    print s.trap(height)

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # 6
    print s.trap(height)