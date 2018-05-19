# coding=utf-8

# 2018-05-17 17:00
# 2018-05-17 17:50 TLE


class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [x[:] for x in [[False] * len(s)] * len(s) ]
        
        for i in range(0, len(s) - 1):
            if s[i] == "(" and s[i + 1] == ")":
                a[i][i + 1] = True
                
        for i in range(0, len(s)):
            for j in range(i, -1, -1): # important reverse
                if i - j == 1 or i == j:
                    continue
                if a[j + 1][i - 1] and s[j] == "(" and s[i] == ")":
                    a[j][i] = True
                else:
                    for k in range(j + 1, i):
                        if a[j][k] and a[k + 1][i]:
                            a[j][i] = True
                            break
        
        max_len = 0
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                if a[i][j]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        
        return max_len
                

# 2018-05-17 17:56
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [0] * (len(s) + 1)
                
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    a[i + 1] = a[i - 1] + 2
                elif s[i - 1] == ")" and (i - 1 - a[i]) >= 0 and s[i - 1 - a[i]] == "(": # important: not crash when underflow
                    a[i + 1] = a[i] + 2 + a[i - 1 - a[i]]
                    
        return max(a)     
        
        
        
        
if __name__ == "__main__":
    s = Solution()
    
    # 0
    str = ")("
    print s.longestValidParentheses(str)
    
    # 6
    str = "()(())"
    print s.longestValidParentheses(str)
    
    # 4
    str = "(()))())("
    print s.longestValidParentheses(str)
    
    # 4
    str = "()()"
    print s.longestValidParentheses(str)
    
    # 4
    str = ")()())"
    print s.longestValidParentheses(str)
    
    # 2
    str = "(()"
    print s.longestValidParentheses(str)
    
    
                