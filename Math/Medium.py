# -*- coding: utf-8 -*-
import collections
import sys
import math


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

    def isUgly_263(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num > 1:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False
        return True

    def nthUglyNumber_264_V1(self, n):  # 可用作归并
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        MAX_INT = sys.maxint
        ugly_number = [
            [1, 2] + [2 * i for i in range(1, n) if i % 2 == 0 or i % 3 == 0 or i % 5 == 0],  # two_ugly_number
            [3] + [3 * i for i in range(1, n) if i % 2 != 0 and (i % 3 == 0 or i % 5 == 0)],  # three_ugly_number
            [5] + [5 * i for i in range(1, n) if i % 2 != 0 and i % 3 != 0 and i % 5 == 0]]  # five_ugly_number
        length, index, count, merge_index, re = len(ugly_number), [0] * len(ugly_number), 0, 0, 0
        print ugly_number
        re = []
        while count < n:
            merge = [ugly_number[i][index[i]] if index[i] < len(ugly_number[i]) else MAX_INT for i in range(length)]
            merge_index = merge.index(min(merge))
            re.append(ugly_number[merge_index][index[merge_index]])

            index[merge_index] += 1
            print merge, '-------------------', merge_index, '==========', index,'++++++',re

            count += 1
        return ugly_number[merge_index][index[merge_index] - 1]

    def nthUglyNumber_264_V2(self, n):  # 遍历Time Limit Exceeded
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        count, num = 1, 2
        while True:
            if self.isUgly_263(num):
                count += 1
                if count == n:
                    return num
            num += 1

    def fractionAddition_592(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b / gcd(a, b)

        part = ''
        fractions = []
        for c in expression:
            if c in '+-':
                if part:
                    print "--------"
                    fractions.append(part)
                part = ''
            part += c
        if part:
            fractions.append(part)

        hi = [int(e.split('/')[0]) for e in fractions]
        lo = [int(e.split('/')[1]) for e in fractions]

        LO = reduce(lcm, lo)
        HI = sum(h * LO / l for h, l in zip(hi, lo))
        GCD = abs(gcd(LO, HI))

        return '%s/%s' % (HI / GCD, LO / GCD)

    """
    *****************************
    """
    def numSquares_279_V1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        re = [0] * (n + 1)
        for i in range(1, n + 1):
            tmp = sys.maxint
            j = 1
            while j * j <= i:

                tmp = min(tmp, re[i - j * j] + 1)
                print re, i, j * j, re[i - j * j] + 1, tmp
                j += 1
            re[i] = tmp
        return re[n]

    def numSquares_279_V2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        while n & 3 == 0:
            n >>= 2
        if n & 7 == 7:
            return 4
        k = int(math.sqrt(n))
        halfk = int(math.sqrt(n/2))
        if k**2 == n:
            return 1
        for j in range(k, halfk-1, -1):
            remain = n - j**2
            remaink = int(math.sqrt(remain))
            if remaink**2 == remain:
                return 2
        return 3

    def numSquares_279_V3(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:  n /= 4

        if n % 8 == 7: return 4

        a = 0
        while a * a <= n:
            b = (math.sqrt(n - a * a))
            b = int(b)

            if a * a + b * b == n:
                if b == 0 or a == 0: return 1
                return 2
            a += 1
        return 3









if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    for i in range(1, 13):
        print(i,"---------",s.numSquares_279(i))








