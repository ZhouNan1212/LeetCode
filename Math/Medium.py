# -*- coding: utf-8 -*-


class Solution(object):
    def complexNumberMultiply_537_V1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_str, b_str = a.split('+'), b.split('+')
        a_real_part, a_imaginary_part, b_real_part, b_imaginary_part = \
            int(a_str[0]), int(a_str[1][0:-1]), int(b_str[0]), int(b_str[1][0:-1]),
        # 实部
        real_part = a_real_part * b_real_part - a_imaginary_part * b_imaginary_part
        # 虚部
        imaginary_part = a_real_part * b_imaginary_part + b_real_part * a_imaginary_part
        return str(real_part) + '+' + str(imaginary_part) + 'i'

    def complexNumberMultiply_537_V2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, b1 = map(int, a[:-1].split("+"))
        a2, b2 = map(int, b[:-1].split("+"))
        return "%s+%si" % (a1*a2-b1*b2, a1*b2+a2*b1)

    def intToRoman_12_V1(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        string = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                  "V", "IV", "I"]
        roman, i = "", 0
        while num != 0:
            if num >= base[i]:
                num -= base[i]
                roman += string[i]
            else:
                i += 1
        return roman

    def intToRoman_12_V2(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.intToRoman_12_V2(130))








