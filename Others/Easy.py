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

    def findComplement_476_V1(self, num):
        """
        :type num: int
        :rtype: int
        """
        re = ""
        for i in list(bin(num).replace("0b", '')):
            if int(i) == 0:
                re += "1"
            else:
                re += "0"
        return int(re, 2)

    def findComplement_476_V2(self, num):
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num

    def getSum_371(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)

    def averageOfLevels_637(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        que = [root]
        while que:
            ans.append(1.0 * sum([n.val for n in que]) / len(que))
            nque = []
            for n in que:
                if n.left: nque.append(n.left)
                if n.right: nque.append(n.right)
            que = nque
        return ans

    def nextGreaterElement_496_V1(self, findNums, nums):  # Time Limit Exceeded
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        re = []
        for index, value in enumerate(findNums):
            index_list = filter(lambda x: nums[x] > value and x >= nums.index(value), range(len(nums)))
            if len(index_list) == 0:
                re.append(-1)
            else:
                re.append(nums[index_list[0]])
        return re

    def nextGreaterElement_496_V2(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        re, second_length = [], len(nums)
        for value in findNums:
            second_index = nums.index(value) + 1
            if second_index > second_length - 1:
                re.append(-1)
                continue
            while second_index < second_length:
                if nums[second_index] > value:
                    re.append(nums[second_index])
                    break
                elif second_index == second_length - 1:
                    re.append(-1)
                    break
                else:
                    second_index += 1
        return re

    def nextGreaterElements_503(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        size = len(nums)
        ans = [-1] * size
        for x in range(size * 2):
            i = x % size
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans

    def calPoints_682_V1(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        re, score = 0, []
        for index, value in enumerate(ops):
            if value.isdigit() or value.replace("-", '').isdigit():
                re += int(value)
                score.append(int(value))
            elif value == "C":
                re -= score.pop()
            elif value == "D":
                mid = score[-1] * 2
                re += mid
                score.append(mid)
            elif value == "+":
                mid = score[-1] + score[-2]
                re += mid
                score.append(mid)
        return re

    def calPoints_682_V2(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        for c in ops:
            if c == 'C':
                score.pop()
            elif c == 'D':
                score.append(score[-1] * 2)
            elif c == '+':
                score.append(score[-1] + score[-2])
            else:
                score.append(int(c))
        return sum(score)

    def findContentChildren_455_V1(self, g, s):  # Time Limit Exceeded
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        re, s = 0, sorted(s)
        for num in g:
            index = 0
            while index < len(s):
                if s[index] >= num:
                    re += 1
                    s.remove(s[index])
                    break
                else:
                    index += 1
        return re

    def findContentChildren_455_V2(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        friend_index, cookie_index, s, g = 0, 0, sorted(s), sorted(g)
        friend_num, cookie_num = len(g), len(s)
        while cookie_index < cookie_num and friend_index < friend_num:
            if s[cookie_index] >= g[friend_index]:
                cookie_index += 1
                friend_index += 1
            else:
                cookie_index += 1
        return friend_index





class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    s = Solution()
    print s.findContentChildren_455_V2([1,2,3], [1,2,3])

