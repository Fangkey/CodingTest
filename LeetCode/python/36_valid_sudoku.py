# coding=utf-8

# 2018-05-18 15:01
# 2018-05-18 15:10

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row
        for i in range(0, 9):
            num_set = set()
            for j in range(0, 9):
                n = board[i][j]
                if n != ".":
                    if n in num_set:
                        return False
                    num_set.add(n)
                    
        # column
        for j in range(0, 9):
            num_set = set()
            for i in range(0, 9):
                n = board[i][j]
                if n != ".":
                    if n in num_set:
                        return False
                    num_set.add(n)
                    
        # block
        for i in range(0, 3):
            for j in range(0, 3):
                num_set = set()
                for k in range(0, 9):
                    ii = i * 3 + k / 3
                    jj = j * 3 + k % 3
                    n = board[ii][jj]
                    if n != ".":
                        if n in num_set:
                            return False
                        num_set.add(n)
                        
        return True
                            

if __name__ == "__main__":
    s = Solution()
    
    board = [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
    # True
    print s.isValidSudoku(board)
                