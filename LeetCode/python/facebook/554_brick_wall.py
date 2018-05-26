# coding=utf-8

#2018-05-24 12:12
#2018-05-24 12:21

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        brick_dict = {}
        for l in wall:
            acc_sum = 0
            for b in l:
                acc_sum += b
                brick_dict[acc_sum] = brick_dict.get(acc_sum, 0) + 1
        
        if len(brick_dict) == 1:
            return len(wall)
        
        sorted_brick_dict = sorted(brick_dict.items(), key=lambda d: d[1], reverse=True)
        return len(wall) - sorted_brick_dict[1][1]
    
    
if __name__ == "__main__":
    s = Solution()
    
    wall = [[1],[1],[1]]
    print s.leastBricks(wall)
    
    wall = [[1,2,2,1],
             [3,1,2],
             [1,3,2],
             [2,4],
             [3,1,2],
             [1,3,1,1]]
    print s.leastBricks(wall)
    
