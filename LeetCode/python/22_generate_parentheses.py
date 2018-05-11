# coding=utf-8

# 2018-05-11 12:48
# 2018-05-11 16:40

class Solution(object):
    def helper(self, n, cur_str, left, right, result):
        if len(cur_str) == 2 * n:
            result.append(cur_str)
        
        if left < n:
            self.helper(n, cur_str + "(", left + 1, right, result)
        if right < left:
            self.helper(n, cur_str + ")", left, right + 1, result)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.helper(n, "", 0, 0, result)
        return result


# 2018-05-11 17:05
class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        
        p_list = []
        for i in range(0, n):
                p_l_list = self.generateParenthesis(i)
                p_r_list = self.generateParenthesis(n - i - 1)
                for pl in p_l_list:
                    for pr in p_r_list:
                        p_list.append("(" + pl + ")" + pr)
        return p_list

if __name__ == "__main__":
    s = Solution1()

    p = s.generateParenthesis(5)
    print p
    print len(p)
    
    p = s.generateParenthesis(4)
    print p
    print len(p)
    
    p = s.generateParenthesis(3)
    print p
    print len(p)
    
    p = s.generateParenthesis(2)
    print p
    print len(p)
    
    p = s.generateParenthesis(1)
    print p
    print len(p)
    
    p = s.generateParenthesis(0)
    print p
    print len(p)