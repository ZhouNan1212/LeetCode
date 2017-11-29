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

    def totalHammingDistance_477_V1(self, nums):  # Time Limit Exceeded
        """
        :type nums: List[int]
        :rtype: int
        """
        index, length, count = 0, len(nums), 0
        while index < length:
            second_index = index + 1
            while second_index < length:
                count += bin(nums[index] ^ nums[second_index]).count('1')
                second_index += 1
            index += 1
        return count

    def totalHammingDistance_477_V2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for x in range(32):
            mask = 1 << x
            zero = one = 0
            for num in nums:
                if num & mask:
                    one += 1
                else:
                    zero += 1
            ans += zero * one
        return ans




if __name__ == '__main__':
    s = Solution()
    print s.totalHammingDistance_477_V2([4, 14, 2])

