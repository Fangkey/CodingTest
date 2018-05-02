class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        dail_pad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = []
        self.helper(dail_pad, digits, [], 0, result)
        return result


    def helper(self, dail_pad, digits, cur_comb, cur_index, result):
        if cur_index == len(digits):
            result.append(''.join(cur_comb))
            return

        cur_digit = digits[cur_index]
        if cur_digit not in dail_pad:
            return

        cur_letter_list = dail_pad[digits[cur_index]]
        for d in cur_letter_list:
            cur_comb.append(d)
            self.helper(dail_pad, digits, cur_comb, cur_index + 1, result)
            cur_comb.pop()

# 2018-05-03 00:17
# 2018-05-03 00:32

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        cur_str = ""
        res_list = []
        self.helper(digit_map, digits, 0, cur_str, res_list)
        return res_list

    def helper(self, digit_map, digits, cur_index, cur_str, res_list):
        if cur_index == len(digits):
            res_list.append(cur_str)
            return

        d = digits[cur_index]
        dc = digit_map[d]

        # only one loop
        for c in dc:
            cur_str += c
            self.helper(digit_map, digits, cur_index + 1, cur_str, res_list)
            cur_str = cur_str[0: -1]


if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations('23')