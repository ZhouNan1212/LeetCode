# -*- coding: utf-8 -*-
import math
class Solution(object):
    def addDigits_258_V1(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = reduce(lambda x, y: int(x) + int(y), list(str(num)))
        return num

    def addDigits_258_V2(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num - 1) % 9 + 1

    def selfDividingNumbers_728(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        re_list = []
        for i in range(left, right + 1):
            digit = list(str(i))
            if "0" not in digit:
                re = sum(map(lambda x: i % int(x), list(str(i))))
                if re == 0:
                    re_list.append(i)
        return re_list

    def titleToNumber_171(self, s):
        """
        :type s: str
        :rtype: int
        """
        each_letter = map(lambda i: ord(i) - 64, s)
        each_postion = map(lambda x: 26 ** x, list(reversed(range(len(s)))))
        re = sum(map(lambda n: n[0] * n[1], zip(each_letter, each_postion)))
        return re


    def convertToTitle_168_V1(self, n):
        """
        :type n: int
        :rtype: str
        """
        re = []
        while n > 0:
            remainder = n % 26
            if remainder == 0:
                re.insert(0, 26)
                div = n / 26 - 1
            else:
                re.insert(0, remainder)
                div = n / 26
            n = div
        title = ""
        for i in re:
            title += chr(i + 64)
        return title

    def convertToTitle_168_V2(self, num):
        """
        :type num: int
        :rtype: str
        """
        return "" if num == 0 else self.convertToTitle_168_V2((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))

    def convertToTitle_168_V3(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ""
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while n:
            ret = letters[n % 26-1] + ret
            n = (n - 1) / 26
        return ret

    def addStrings_415(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = max(len(num1), len(num2))
        num1_str, num2_str, re = num1.zfill(length), num2.zfill(length), ""  # 将两个字符串长度补齐
        num1_str_list, num2_str_list = list(num1_str), list(num2_str)
        each_digit = map(lambda x: int(x[0]) + int(x[1]), zip(num1_str_list, num2_str_list))

        index = len(each_digit) - 1
        while index > 0:
            if each_digit[index] > 9:
                each_digit[index - 1] += each_digit[index] / 10
                each_digit[index] = each_digit[index] % 10
                print each_digit[index - 1]
            index -= 1
        return "".join(map(str, each_digit))

    def mySqrt_69(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))

    def isPerfectSquare_367_V1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    def isPerfectSquare_367_V2(self, num):
        return int(num**0.5) == num**0.5

    def isPerfectSquare_367_V3(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sq = num/2.0
        while abs(sq*sq - num) > 0.000001:
            sq = (sq + num/sq)/2
        return round(sq)*round(sq) == num

    def superPow_372_V1(self, a, b):  # Time Limit Exceeded
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        num = int("".join(map(str, b)))
        return a ** num % 1337

    def superPow_372_V2(self, a, b):
        res = 1
        s = Solution()
        for i in b:
            res = s.support_pow(res, 10) * s.support_pow(a, int(i)) % 1337
        return res

    @staticmethod
    def support_pow(x, n):
        if n == 0:
            return 1
        if n == 1:
            return x % 1337
        return pow(x % 1337, n / 2) * pow(x % 1337, n - n / 2) % 1337

    def superPow_372_V3(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod1 = mod = a % 1337
        period = 0
        while True:  # search for period
            mod = mod * mod1 % 1337
            period += 1
            if mod == mod1:
                break
        b = int(''.join(str(i) for i in b))  # python is sweet, it has built-in bigint support
        b_adjusted = b % period
        return (mod ** b_adjusted) % 1337


class Judge(object):  # Time Limit Exceeded
    """
    正整数M能表示成两个整数平方和的充要条件是：M的素因子分解式重所有形如4n-1的素因子的幂指数都是偶数
    """

    # 判断是否是素数
    @staticmethod
    def isprime(num):
        count = num / 2
        while count > 1:
            if num % count == 0:
                return False
            count -= 1
        else:
            return True

    # 得到所有的约数
    @staticmethod
    def getfactors(num):
        return [x for x in range(1, num) if num % x == 0]

    # 分解
    @staticmethod
    def primefactor(num):
        s = Judge()
        if s.isprime(num):
            return [1, num]
        factors = s.getfactors(num)
        retList = []
        consult = num
        for i in range(1, len(factors)):
            if consult == 1:
                break
            while True:
                if consult % factors[i] != 0:
                    break
                if s.isprime(factors[i]):
                    consult /= factors[i]
                    retList.append(factors[i])
                else:
                    break
        return retList

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        s = Judge()
        factors_list = s.primefactor(c)
        all_factors = set(factors_list)
        for i in all_factors:
            if (i + 1) % 4 == 0 and factors_list.count(i) % 2 != 0:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.superPow_372_V2(2,[1,0]))

