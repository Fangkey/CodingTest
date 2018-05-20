# coding=utf-8

# valid palindrome with space and punctuation
# legal example:
#   12321
#   A man, a plan, a canal, Panama!

# 2018-05-19 23:09
# 2018-05-19 23:15

class Solution(object):
    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if not self.is_legal(s[i]):
                i += 1
            elif not self.is_legal(s[j]):
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

    def is_legal(self, s):
        return s.isdigit() or s.isalpha()


if __name__ == "__main__":
    s = Solution()

    string = "A man, a plan, a canal, Panama!"
    print s.is_palindrome(string)

    string = "12321"
    print s.is_palindrome(string)

    string = "valid palindrome"
    print s.is_palindrome(string)