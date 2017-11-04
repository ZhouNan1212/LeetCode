# -*- coding: utf-8 -*-
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = [1]
        for x in range(k):
            m = ans[-1] + [1, -1][x % 2] * (k - x)
            ans.append(m)
        return ans + range(k + 2, n + 1)

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        for i in range(len(nums) - 1):
            left.append(nums[i] * left[-1])
        right = [1]
        nums.reverse()
        for j in range(len(nums) - 1):
            right.insert(0, nums[j] * right[0])
        for index in range(len(nums)):
            nums[index] = left[index] * right[index]
        return nums

    def combinationSum3(self, k, n):
        ans = []

        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                ans.append(nums)
                return
            for x in range(start + 1, 10):
                search(x, cnt + 1, sums + x, nums + [x])
        search(0, 0, 0, [])
        return ans

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while True:
            slow, fast = nums[slow], nums[fast]
            if slow == fast:
                return slow

    def findErrorNumsV1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_set = set()
        duplicate, length = 0, len(nums)
        nums_sum = (length * (1 + length)) / 2
        for i in nums:
            if i in new_set:
                duplicate = i
            else:
                new_set.add(i)
            nums_sum -= i
        return [duplicate, nums_sum + duplicate]

    def findErrorNumsV2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums = [a1, a1, a3], 理论上应该是[a1, a2, a3]
        n = len(nums)
        alpha = sum(nums) - n * (n + 1) / 2  # a1 - a2
        beta = (sum(map(lambda x: x * x, nums)) - n * (n + 1) * (2 * n + 1) / 6) / alpha  # a1 + a2
        return [(alpha + beta) / 2, (beta - alpha) / 2]

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.findErrorNumsV2([1,2,2]))
