# coding=utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(0, n - 1):
            cur_l = s[0]
            new_s = ""
            cnt = 0
            for j in range(0, len(s)):
                if cur_l == s[j]:
                    cnt += 1
                else:
                    new_s += (str(cnt) + cur_l)
                    cur_l = s[j]
                    cnt = 1
            new_s += str(cnt) + cur_l
            s = new_s
            
        return s
    
if __name__ == "__main__":
    s = Solution()
    
    print s.countAndSay(1)
    print s.countAndSay(2)
    print s.countAndSay(3)
    print s.countAndSay(4)
    print s.countAndSay(5)