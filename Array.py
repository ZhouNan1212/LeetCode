# -*- coding: utf-8 -*-
from scipy.special import comb
import copy

class Solution(object):
    def getRowV1(self, row_index):  # 帕斯卡三角的的每行值，是对应的二项式(a + b)^n的展开系数，使用二项式定理
        """
        :type row_index: int
        :rtype: List[int]
        """
        re = (row_index + 1) * [1]
        for i in range(1, row_index):  # [from, to)
            re[i] = int(comb(row_index, i))  # 当row_index比较大时，会遇到精度问题
        return re

    def getRowV2(self, row_index):
        re = [1]
        for index in range(1, row_index + 1):
            re.insert(0, 1)
            j = 1
            while j < len(re) - 1:
                re[j] += re[j + 1]
                j += 1
        return re

    def removeDuplicatesV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                del nums[index + 1]
            else:
                index += 1
        return len(nums)

    def removeDuplicatesV2(self, nums):
        last = None
        length = 0
        for n in nums:
            if n != last:
                nums[length] = last = n
                length += 1
        return length

    def canPlaceFlowersV1(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        new_flower = 0
        index = 0
        length = len(flowerbed)
        while index < length:
            if flowerbed[index] == 0:
                if index == 0:
                    left = 0
                    right = min(1, length - 1)
                elif index == length - 1:
                    left = length - 2
                    right = length - 1
                else:
                    left = max(index - 1, 0)  # 避免数组越界
                    right = min(index + 1, length - 1)
                if flowerbed[left] == 0 and flowerbed[right] == 0:  # python的与或非要用关键字 and or
                    flowerbed[index] = 1
                    new_flower += 1
            if index == length - 2:  # 倒数第二个加1，其他情况加2
                index += 1
            else:
                index += 2
        if new_flower >= n:
            return True
        else:
            return False

    def canPlaceFlowersV2(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        for i in xrange(len(flowerbed)):
            f = flowerbed[i]
            if f == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                cnt += 1
        if cnt >= n:
            return True
        return False

    def findUnsortedSubarrayV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_list = copy.deepcopy(nums)  # 深拷贝
        tmp_list = sorted(tmp_list)
        start = 0
        end = len(nums) - 1
        while start < len(nums) and tmp_list[start] == nums[start]:
            start += 1
        while end > start and tmp_list[end] == nums[end]:
            end -= 1
        return end + 1 - start

    def findUnsortedSubarrayV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return 0
        i = 0
        while i + 1 < len(nums) and nums[i] <= nums[i + 1]:
            i += 1
        if i == len(nums) - 1:
            return 0
        j = len(nums) - 1
        while j - 1 >= 0 and nums[j - 1] <= nums[j]:
            j -= 1
        minv, maxv = min(nums[i:j + 1]), max(nums[i:j + 1])
        while i >= 0 and nums[i] > minv:
            i -= 1
        while j < len(nums) and nums[j] < maxv:
            j += 1
        return j - i - 1

    def findPairsV1(self, nums, k):  # Time Limit Exceeded
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = 0
        new_nums = list(set(copy.deepcopy(nums)))
        if k > 0:
            for first_index in range(len(new_nums) - 1):
                for second_index in range(first_index, len(new_nums)):
                    if abs(new_nums[first_index] - new_nums[second_index]) == k:
                        pairs += 1
        elif k == 0:
            if len(new_nums) != len(nums):
                elements_count = {}
                for value in nums:
                    if value in elements_count.keys():
                        elements_count[value] += 1
                    else:
                        elements_count[value] = 1
                return len([value for value in elements_count.values() if value > 1])
        else:
            pass
        return pairs





if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.findPairs([1,1,1,2,2], 0))

