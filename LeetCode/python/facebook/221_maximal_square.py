# coding=utf-8


# 2018-05-26 16:57
# 2018-05-26 

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        h = len(matrix)
        if h == 0:
            return 0
        
        w = len(matrix[0])
        
        a = [x[:] for x in [[0] * (w + 1)] * (h + 1)]
        
        max_size = 0
        for i in range(0, h):
            for j in range(0, w):
                if matrix[i][j] == "1":
                    a[i + 1][j + 1] = min([a[i + 1][j], a[i][j + 1], a[i][j]]) + 1
                    if a[i + 1][j + 1] > max_size:
                        max_size = a[i + 1][j + 1]
                    
        return max_size ** 2
    
if __name__ == "__main__":
    s = Solution()
    m = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]

    print s.maximalSquare(m)
    
                    
                                
                
                
        