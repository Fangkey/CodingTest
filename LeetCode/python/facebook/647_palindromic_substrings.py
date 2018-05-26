# coding=utf-8

# 2018-05-26 16:27
# 2018-05-26 16:42

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        a = [x[:] for x in [[False] * len(s)] * len(s)]
        
        for i in range(0, len(s)):
            a[i][i] = True
            
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                a[i][i + 1] = True
            
        for i in range(1, len(s)):
            for j in range(0, i):
                if i - j > 1:
                    if s[i] == s[j] and a[j + 1][i - 1]:
                        a[j][i] = True
        
        count = 0
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                if a[i][j]:
                    count += 1
                    
        return count
    
if __name__ == "__main__":
    s = Solution()
    
    # 6
    ss = "aaa"
    print s.countSubstrings(ss)
    
    # 3
    ss = "abc"
    print s.countSubstrings(ss)
    
    