# -*- coding: utf-8 -*-
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


if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.groupAnagramsV2(["eat", "tea", "tan", "ate", "nat", "bat"]))
