class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            mid_x = mid / n
            mid_y = mid % n
            mid_v = matrix[mid_x][mid_y]
            if mid_v == target:
                return True
            elif mid_v < target:
                start = mid
            elif mid_v > target:
                end = mid

        if matrix[start / n][start % n] == target:
            return True
        elif matrix[end / n][end % n] == target:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print s.searchMatrix(
        [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ], 100)
