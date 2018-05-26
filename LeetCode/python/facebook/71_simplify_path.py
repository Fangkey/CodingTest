# coding=utf-8

# 2018-05-26 13:01
# 2018-05-26 13:09

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        
        dirs = path.split("/")
        for d in dirs:
            if d == "":
                continue
            if d == ".":
                continue
            if d == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(d)
                
        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    
    # /home
    path = "/home/"
    print s.simplifyPath(path)
    # /c
    path = "/a/./b/../../c/"
    print s.simplifyPath(path)
    # /
    path = "/../"
    print s.simplifyPath(path)
    # /home/foo
    path = "/home//foo/"
    print s.simplifyPath(path)                    
    # /e/f/g
    path = "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"
    print s.simplifyPath(path)
                
            
            