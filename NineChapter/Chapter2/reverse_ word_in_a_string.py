class Solution(object):
    def reverse(self, a, start, end):
        while start < end:
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
            start += 1
            end -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(" ")
        filtered_word_list = [w for w in word_list if w != ""]
        str_list = list(" ".join(filtered_word_list))
        found_start = False
        start = 0
        for i in range(0, len(str_list)):
            if str_list[i] != " ":
                if not found_start:
                    found_start = True
                    start = i
            else:
                if found_start:
                    found_start = False
                    self.reverse(str_list, start, i - 1)

        if found_start:
            self.reverse(str_list, start, len(str_list) - 1)

        self.reverse(str_list, 0, len(str_list) - 1)
        return "".join(str_list)


if __name__ == "__main__":
    s = Solution()
    string = "the sky is blue"
    print s.reverseWords(string)

    string = "      the sky is blue"
    print s.reverseWords(string)


    string = "      the    sky is blue   "
    print s.reverseWords(string)

    string = "    "
    print s.reverseWords(string)

    string = ""
    print s.reverseWords(string)