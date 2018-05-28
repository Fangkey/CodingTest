# coding=utf-8

# 2018-05-29 00:52
# 2018-05-29 00:57 TLE

class Solution1(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        step = [(1, -2), (2, -1),
                (2, 1), (1, 2),
                (-1, 2), (-2, 1),
                (-2, -1), (-1, -2)
                ]
        count = [0]
        self.helper(N, step, r, c, K, count)
        return float(count[0]) / (8 ** K)

    def helper(self, N, step, x, y, cur_k, count):
        if cur_k == 0:
            count[0] += 1
            return

        for s in step:
            new_x = x + s[0]
            new_y = y + s[1]
            if new_x >=0 and new_x < N and new_y >= 0 and new_y < N:
                self.helper(N, step, new_x, new_y, cur_k - 1, count)

# 2018-05-29 01:09
# 2018-05-29 01:36 DP
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0:
            return 1

        step = [ (1, -2), (2, -1),
                 (2, 1), (1, 2),
                 (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2)]

        a = [x[:] for x in [[0] * N] * N]

        for s in step:
            new_x = r + s[0]
            new_y = c + s[1]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                a[new_x][new_y] = 1

        for i in range(1, K):
            new_state = [x[:] for x in [[0] * N] * N]
            for x in range(0, N):
                for y in range(0, N):
                    s_sum = 0
                    for s in step:
                        new_x = x + s[0]
                        new_y = y + s[1]
                        if new_x >=0 and new_x < N and new_y >= 0 and new_y < N:
                            s_sum += a[new_x][new_y]
                    new_state[x][y] = s_sum

            a = new_state

        all_sum = sum([sum(ss) for ss in a])
        return float(all_sum) / (8 ** K)

if __name__ == "__main__":
    s = Solution()

    # 0.01562
    print s.knightProbability(3, 3, 0, 0)

    # 1
    print s.knightProbability(1, 0, 0, 0)
    # 0.0625
    print s.knightProbability(3, 2, 0, 0)