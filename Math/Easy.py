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
        re = []
        for i in s:
            print i
            re += ord(i) - 64
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

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    for i in range(10, 70):
        print(s.convertToTitle_168_V3(i))

