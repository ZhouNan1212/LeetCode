# -*- coding: utf-8 -*-
import collections


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

    def originalDigits_423_V1(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        观察英文单词，six, zero, two, eight, seven, four中分别包含唯一字母x, z, w, g, v, u；
        因此6, 0, 2, 8, 7, 4需要排在其余数字之前。排除这6个数字之后，剩下的4个数字中，按照字母唯一的原则顺次挑选。
        由于剩下的单词中，只有five包含f，因此选为下一个单词；
        """
        cnts = collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]

        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] / cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for c in cntn:
                cnts[c] -= t * cntn[c]
        return ''.join(str(i) * n for i, n in enumerate(ans))

    def originalDigits_423_V2(self, s):
        zero = s.count('z')
        eight = s.count('g')
        two = s.count('w')
        six = s.count('x')
        three = s.count('h') - eight
        seven = s.count('s') - six
        five = s.count('v') - seven
        four = s.count('f') - five
        one = s.count('o') - four - two - zero
        nine = s.count('i') - five - six - eight
        return ('0'*zero +
                '1'*one +
                '2'*two +
                '3'*three +
                '4'*four +
                '5'*five +
                '6'*six +
                '7'*seven +
                '8'*eight +
                '9'*nine)

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.originalDigits_423("owoztneoer"))








