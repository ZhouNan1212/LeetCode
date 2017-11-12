# -*- coding: utf-8 -*-
import collections


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {"q": 1, "w": 1, "e": 1, "r": 1, "t": 1, "y": 1, "u": 1, "i": 1, "o": 1, "p": 1,
                    "a": 2, "s": 2, "d": 2, "f": 2, "g": 2, "h": 2, "j": 2, "k": 2, "l": 2,
                    "z": 3, "x": 3, "c": 3, "v": 3, "b": 3, "n": 3, "m": 3,
                    "Q": 1, "W": 1, "E": 1, "R": 1, "T": 1, "Y": 1, "U": 1, "I": 1, "O": 1, "P": 1,
                    "A": 2, "S": 2, "D": 2, "F": 2, "G": 2, "H": 2, "J": 2, "K": 2, "L": 2,
                    "Z": 3, "X": 3, "C": 3, "V": 3, "B": 3, "N": 3, "M": 3}
        one_row_word = []
        for word in words:
            re = map(lambda x: keyboard[x], word)
            if len(list(set(re))) == 1:
                one_row_word.append(word)
        return one_row_word

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) / 2)

    def groupAnagramsV1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        re, output = {}, []
        for string in strs:
            key = "".join(sorted(string))
            re[key] = re.get(key, [])  # 应该先get再append，否则如果不存在该键就会出错
            re[key].append(string)
        for value in re.values():
            output.append(value)
        return output

    def groupAnagramsV2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        res = []
        for string in strs:
            formatted = ''.join(sorted(string))
            if formatted not in store:
                store[formatted] = len(res)
                res.append([string])
            else:
                res[store[formatted]].append(string)
        return res

    def isAnagramV1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagramV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        默认字典,是字典的一个子类,继承有字典的方法和属性,
        默认字典在进行定义初始化的时候可以指定字典值得默认类型,
        例如字典中没有key = 2，执行dic[2]依然可以返回结果0.
        """
        histogram = collections.defaultdict(int)
        for char in s:
            histogram[char] += 1
        for char in t:
            histogram[char] -= 1

        differences = sum([abs(histogram[x]) for x in histogram])
        return differences == 0

    def findTheDifferenceV1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        histogram = collections.defaultdict(int)
        for char in s:
            histogram[char] += 1
        for char in t:
            histogram[char] -= 1
        for key in histogram.keys():
            if histogram[key] != 0:
                return key

    def findTheDifferenceV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return t

        """
        ord()函数主要用来返回对应字符的ascii码，
        chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。
        """
        result = ord(s[0]) ^ ord(t[0])
        for i in xrange(1, len(s)):
            result ^= ord(s[i]) ^ ord(t[i])

        return chr(result ^ ord(t[-1]))

    def intersectionV1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        letters, re = set(nums1), set()
        for string in nums2:
            if string in letters:
                re.add(string)
        return list(re)

    def intersectionV2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersectionV2(nums2, nums1)  # 始终遍历较长的一个数组
        nums1Set = set(nums1)
        res = []
        for num2 in nums2:
            if num2 in nums1Set:
                res.append(num2)
                nums1Set.discard(num2)  # 如果存在元素，就删除；没有不报异常
        return res

    def frequencySortV1(self, s):
        """
        :type s: str
        :rtype: str
        """
        histogram = collections.defaultdict(int)
        for char in s:
            histogram[char] += 1
        dic = sorted(histogram.items(), key=lambda d: d[1], reverse=True)
        re = ""
        for key, value in dic:
            re += key * value
        return re

    def frequencySortV2(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_map = {c: s.count(c) for c in set(s)}  # 字符串的count方法更方便

        # convert to list to sorted by count
        by_freq = sorted([(v, k) for k, v in freq_map.items()], reverse=True)

        # turn list of tuples into output string
        output = [t[1] * t[0] for t in by_freq]

        return ''.join(output)



if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.frequencySort("aabbbbc"))
