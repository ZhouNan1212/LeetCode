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

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print s.detectCapitalUse_520_V2("leeTcode")
