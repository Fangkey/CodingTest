# coding=utf-8

# 2018-05-10 17:51
# 2018-05-10 16:04

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if len(stack) == 0:
                if p == ")" or p == "}" or p == "]":
                    return False
                stack.append(p)
            else:
                if p == ")" or p == "}" or p == "]":
                    top = stack[-1]
                    if (top == "(" and p != ")") or top == "[" and p != "]" or top == "{" and p != "}":
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(p)
                    
        if len(stack) == 0:
            return True
        else:
            return False
                    

if __name__ == "__main__":
    s = Solution()
    
    # T
    print s.isValid("()[]{}")
    # F
    print s.isValid("(]")
    # F
    print s.isValid("([)]")
    # T
    print s.isValid("{[]}")
    