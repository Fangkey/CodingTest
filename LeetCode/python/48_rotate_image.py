# coding=utf-8

# 2018-05-20 03:48
# 2018-05-20 04:16

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        h = len(matrix)

        if h == 0:
            return

        for i in range(0, h / 2):
            j = i
            l = h - 2 * j
            for k in range(j, j + l - 1):
                lt = matrix[i][k]
                rt = matrix[i + k - j][h - 1 - j]
                rb = matrix[h - 1 - i][h - 1 - k]
                lb = matrix[h - 1 - k][j]

                matrix[i][k] = lb
                matrix[i + k - j][h - 1 - j] = lt
                matrix[h - 1 - i][h - 1 - k] = rt
                matrix[h - 1 - k][j] = rb


if __name__ == "__main__":
    s = Solution()

    matrix = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
    s.rotate(matrix)
    print matrix

    matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    s.rotate(matrix)
    print matrix


