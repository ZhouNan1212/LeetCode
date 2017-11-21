# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution(object):
    """
    有点操蛋，总是不对
    """
    def smallestRange_632(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        list_index, complete_list, count = 0, [], {}
        while list_index < len(nums):  # 将所有有序数组归并
            list_element_index, count[list_index] = 0, len(nums[list_index])
            while list_element_index < len(nums[list_index]):
                complete_list.append((list_index, nums[list_index][list_element_index]))
                list_element_index += 1
            list_index += 1
        complete_list = sorted(complete_list, key=lambda i: i[1])
        if len(nums) == 1:
            return [complete_list[0][1]]

        left, right, count_class, re = 0, 1, [0]*len(nums), [0, len(complete_list)]
        count_class[complete_list[left][0]] += 1
        count_class[complete_list[right][0]] += 1
        print complete_list

        while left < len(complete_list) - 1:
            if 0 in count_class:
                if right < len(complete_list) - 1:
                    right += 1
                    count_class[complete_list[right][0]] += 1
                else:
                    break
            elif re[1] - re[0] > complete_list[right][1] - complete_list[left][1] or (re[1] - re[0] == complete_list[right][1] - complete_list[left][1] and re[0] > complete_list[left][1]):
                re[1], re[0] = complete_list[right][1], complete_list[left][1]
            else:
                count_class[complete_list[left][0]] -= 1
                left += 1
        return re

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.smallestRange_632([[47,67,82,97],[-2,34,42,49,50,50,51],[-61,-45,-3,-1,2,10],[25,57,76,77,78],[-11,10,29,55,55,55,57,59,60,60,62,63]]))
