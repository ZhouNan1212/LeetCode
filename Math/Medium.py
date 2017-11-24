# -*- coding: utf-8 -*-


class Solution(object):
    def complexNumberMultiply_537(self, a, b):
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

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.complexNumberMultiply_537( "1+-1i", "1+-1i"))








