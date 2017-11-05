class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0

        d = []
        d.append([triangle[0][0]])
        for i, l in enumerate(triangle[1: ]):
            dl = []
            for j, n in enumerate(l):
                if j == 0:
                    dl.append(d[i][0] + l[0])
                elif j == len(l) - 1:
                    dl.append(d[i][j - 1] + l[j])
                else:
                    m = min(d[i][j-1], d[i][j])
                    dl.append(m + l[j])
            d.append(dl)

        return min(d[-1])


if __name__ == "__main__":
    s = Solution()
    t = [[-1], [-2, -3]]

    print s.minimumTotal(t)

    t = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

    print s.minimumTotal(t)