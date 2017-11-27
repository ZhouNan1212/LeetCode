# -*- coding: utf-8 -*-
class Solution(object):
    def detectCapitalUse_520_V1(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length = len(word)
        index = filter(lambda i: word[i].islower(), range(length))
        if len(index) in [0, length]:
            return True
        elif len(index) == length - 1 and index[0] == 1:
            return True
        return False

    def detectCapitalUse_520_V2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        """
        isupper(): 方法检测字符串是否由大写字母组成
        islower(): 方法检测字符串是否由小写字母组成
        istitle(): 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
        any(): 方法用于判断给定的可迭代参数iterable是否全部为空对象，如果不都为空、0、false，则返回 True。
        all(): 方法用于判断给定的可迭代参数iterable是否全部为空对象，如果不都为空、0、false，则返回 False。
        """
        return any((word.isupper(), word.islower(), word.istitle()))

    def reverseWords_557(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda n: n[::-1], s.split(' ')))  # 这里用列表推导式也可以
        # return " ".join([n[::-1] for n in s.split(' ')])

    def canConstruct_383(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = set(ransomNote)
        for i in letters:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

    def compress_443_V1(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        """
        这题的OJ系统判断很奇怪，并没有检查返回的整数是否正确，而是检查chars是否正确
        """
        count = {a: chars.count(a) for a in set(chars)}  # 字典推导式
        letter_sort = sorted(count.iteritems(), key=lambda d: d[0])
        re = []
        for x, y in letter_sort:
            if y > 1:
                re.append(x)
                re += list(str(y))
            else:
                re.append(x)
        return len(re)

    def countSegments_434(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(filter(lambda x: len(x) > 0, s.split(' ')))

    def isValid_20(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        re, pattern = [], {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in ["(", "[", "{"]:
                re.append(char)
            elif len(re) == 0 or (len(re) > 0 and pattern[char] != re.pop()):
                return False
        return len(re) == 0



if __name__ == '__main__':
    s = Solution()
    print s.isValid_20('')
