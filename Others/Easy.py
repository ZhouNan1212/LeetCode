# -*- coding: utf-8 -*-
class Solution(object):
    def hammingDistance_461_V1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin_str, y_bin_str = bin(x).replace('0b', ''), bin(y).replace('0b', '')
        max_length = max(len(x_bin_str), len(y_bin_str))
        bin_str = zip(list(x_bin_str.zfill(max_length)), list(y_bin_str.zfill(max_length)))
        return len(filter(lambda n: n[0] != n[1], bin_str))

    def hammingDistance_461_V2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        z = x ^ y
        while z:
            distance += 1
            z &= z - 1
        return distance

    def hammingDistance_461_V3(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')




if __name__ == '__main__':
    s = Solution()
    print s.hammingDistance_461_V1(1, 4)

