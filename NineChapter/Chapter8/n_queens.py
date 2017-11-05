class Solution(object):
    def check(self, solution, i, j):
        for c, r in enumerate(solution):
            if r == i:
                return False
            if (j - c) == (i - r) or (j - c) == (r - i):
                return False
        return True

    def helper(self, n, solution, result):
        cur_j = len(solution)
        if cur_j == n:
            result.append(solution[:])
            return

        for i in range(0, n):
            if solution == [1, 3]:
                pass
            if self.check(solution, i, cur_j):
                solution.append(i)
                self.helper(n, solution, result)
                solution.pop()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.helper(n, [], result)

        ret = []
        for s in result:
            s_str_list = []
            for c in s:
                c_str = ""
                for i in range(0, n):
                    if i == c:
                        c_str += "Q"
                    else:
                        c_str += "."
                s_str_list.append(c_str)
            ret.append(s_str_list)

        return ret


if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)
