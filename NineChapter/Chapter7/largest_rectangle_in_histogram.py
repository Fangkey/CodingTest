class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0

        heights.append(0)

        stack = []
        stack.append((-1, -1))

        max_rect = 0

        for i in range(0, len(heights)):
            h = heights[i]
            if h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while len(stack) != 0 and h < stack[-1][1]:
                    cur_i, cur_h = stack.pop()
                    # important
                    cur_rect = (i - stack[-1][0] - 1) * cur_h
                    if cur_rect > max_rect:
                        max_rect = cur_rect
                stack.append((i, h))

        return max_rect


if __name__ == "__main__":
    s = Solution()

    # 3
    print s.largestRectangleArea([2, 1, 2])
    # 10
    print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    # 2
    print s.largestRectangleArea([1,1])



