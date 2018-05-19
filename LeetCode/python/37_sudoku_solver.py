# coding=utf-8

# 2018-05-18 15:16
# 2018-05-18 16:38 Trapped by a tiny bug, reverse the index of blk_check...

class Solution(object):
    def __init__(self):
        self.row_check = []
        self.col_check = []
        self.blk_check = []
        
        
    def init_check_set(self, board):
        self.row_check = []
        self.col_check = []
        self.blk_check = []
        
        cnt = 0
        # row
        for i in range(0, 9):
            num_set = set()
            for j in range(0, 9):
                n = board[i][j]
                if n != ".":
                    cnt += 1
                    num_set.add(int(n))
            self.row_check.append(num_set)
            
        # col
        for j in range(0, 9):
            num_set = set()
            for i in range(0, 9):
                n = board[i][j]
                if n != ".":
                    num_set.add(int(n))
            self.col_check.append(num_set)
                
        # blk
        for i in range(0, 3):
            for j in range(0, 3):
                num_set = set()
                for k in range(0, 9):
                    ii = i * 3 + k / 3
                    jj = j * 3 + k % 3
                    n = board[ii][jj]
                    if n != ".":
                        num_set.add(int(n))
                self.blk_check.append(num_set)
                
        return cnt
            
    def is_valid(self, i, j, n):
        n = int(n)
        # row
        row_check_set = self.row_check[i]
        if n in row_check_set:
            return False
        
        # col
        col_check_set = self.col_check[j]
        if n in col_check_set:
            return False
        
        # blk
        bi = i / 3
        bj = j / 3
        blk_check_set = self.blk_check[bi * 3 + bj]
        if n in blk_check_set:
            return False
        
        return True
    
    def add_to_check(self, i, j, n):
        n = int(n)
        # row
        self.row_check[i].add(n)
        
        # col
        self.col_check[j].add(n)
    
        # blk
        bi = i / 3
        bj = j / 3
        self.blk_check[bi * 3 + bj].add(n)

    def rm_from_check(self, i, j, n):
        n = int(n)
        # row
        self.row_check[i].remove(n)
        
        # col
        self.col_check[j].remove(n)
    
        # blk
        bi = i / 3
        bj = j / 3
        self.blk_check[bi * 3 + bj].remove(n)
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        num_cnt = self.init_check_set(board)
        
        solve_board = [x[:] for x in [[0] * 9] * 9]
        
        
        self.helper(board, solve_board, 0)
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    board[i][j] = str(solve_board[i][j])
        
        return
    
    def helper(self, board, solve_board, c):
        if c == 81:
            return True
    
        i = c / 9
        j = c % 9
        
        if board[i][j] != ".":
            return self.helper(board, solve_board, c + 1)
        else:
            for nn in range(1, 10):
                if self.is_valid(i, j, nn):
                    solve_board[i][j] = nn
                    self.add_to_check(i, j, nn)
                    if self.helper(board, solve_board, c + 1):
                        return True
                    self.rm_from_check(i, j, nn)
                    solve_board[i][j] = 0


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
    s.solveSudoku(board)
    print board
        
        
        
        
        
        