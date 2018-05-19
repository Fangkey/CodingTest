# coding=utf-8

# 2018-05-15 17:22
# 2018-05-16 13:14

class Solution(object):  
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import sys
        
        dict_t = {}
        for l in t:
            dict_t[l] = dict_t.get(l, 0) + 1
            
        begin = 0
        end = 0
        count = len(t)
        min_len = sys.maxint
        min_begin = 0
        min_end = 0
        
        while end < len(s):
            l_end = s[end]
            if l_end in dict_t:
                if dict_t[l_end] > 0:
                    count -= 1
                dict_t[l_end] -= 1
            end += 1
            
            while count == 0:
                if end - begin < min_len:
                    min_len = end - begin
                    min_begin = begin
                    min_end = end
                    
                l_begin = s[begin]
                if l_begin in dict_t:
                    if dict_t[l_begin] >= 0:
                        count += 1
                    dict_t[l_begin] += 1
                begin += 1
        
        return s[min_begin: min_end]
    
if __name__ == "__main__":
    s = Solution()
    
    source = "bba"
    target = "ab"
    # "ba"
    print s.minWindow(source, target)
    
    source = "ab"
    target = "a"
    # a
    print s.minWindow(source, target)
    
    source = "a"
    target = "aa"
    # ""
    print s.minWindow(source, target)
    
    source = "ADOBECODEBANC"
    target = "ABC"
    # BANC
    print s.minWindow(source, target)
                    
                    
                    
                    
                    
                    
                    