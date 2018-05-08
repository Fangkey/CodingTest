# coding=utf-8

# 2018-05-09 00:51
# 2018-05-09 01:33

class Solution(object):
    def helper(self, board, h, w, t, i, j, word, cur):
        l = word[cur]
        if l == board[i][j]:
            if cur + 1 == len(word):
                return True

            t[i][j] = 1
            r_down = False
            if i + 1 < h and t[i + 1][j] == 0:
                r_down = self.helper(board, h, w, t, i + 1, j, word, cur + 1)

            r_up = False
            if i - 1 >= 0 and t[i - 1][j] == 0:
                r_up = self.helper(board, h, w, t, i - 1, j, word, cur + 1)

            r_right = False
            if j + 1 < w and t[i][j + 1] == 0:
                r_right = self.helper(board, h, w, t, i, j + 1, word, cur + 1)

            r_left = False
            if j - 1 >= 0 and t[i][j - 1] == 0:
                r_left = self.helper(board, h, w, t, i, j - 1, word, cur + 1)

            if r_left or r_right or r_up or r_down:
                return True
            else:
                # track back, important
                t[i][j] = 0
                return False
        else:
            return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        h = len(board)
        if h == 0:
            return False
        w = len(board[0])

        found = False
        t = [x[:] for x in [[0] * w] * h]
        for i in range(0, h):
            for j in range(0, w):

                if self.helper(board, h, w, t, i, j, word, 0):
                    found = True
                    break
            if found:
                break

        return found


if __name__ == "__main__":
    s = Solution()
    b = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print s.exist(b, word)

    b = [
        ['A'],
    ]
    word = "A"
    print s.exist(b, word)

    b =[
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
    word = "ABCB"
    print s.exist(b, word)

    word = "ABCCED"
    print s.exist(b, word)

    word = "SEE"
    print s.exist(b, word)


