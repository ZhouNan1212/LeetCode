# -*- coding: utf-8 -*-
from scipy.special import comb
from math import factorial

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

    def singleNumberV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * reduce(lambda x, y: x + y, list(set(nums))) - reduce(lambda x, y: x + y, nums)

    def singleNumberV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
            print res
        return res

    def firstMissingPositiveV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = list(set(filter(lambda x: x > 0, nums)))
        if len(nums) == 0 or len(new_nums) == 0:
            return 1
        new_nums = zip(sorted(new_nums), range(1, len(new_nums) + 1))
        re = None
        for element in new_nums:
            if element[0] != element[1]:
                re = element[1]
                break
        if re is not None:
            return re
        else:
            return new_nums[-1][1] + 1

    def firstMissingPositiveV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 1
        nums.sort()
        nums = [i for i in nums if (i >= 0)]
        if nums[0] > 1:
            return 1
        for i in range(0, len(nums) - 1):
            if nums[i] + 1 != nums[i + 1] and nums[i] != nums[i + 1]:
                return nums[i] + 1
        return nums[len(nums) - 1] + 1

    def subsetsV1(self, nums):  # 位运算
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1 << len(nums)):
            subset = []
            for j in range(len(nums)):
                if i & 1 << j:
                    subset.append(nums[j])
            result.append(subset)
        return result

    def subsetsV2(self, nums):  # 回溯法
        res = [[]]
        for num in sorted(nums):
            print res
            res += [item + [num] for item in res]
        return res

    def sortedNums(self, nums):
        return sorted(nums)

    def zipNums(self, nums):
        return zip(nums, nums[1:], nums[2:])

    def judgeTriangle(self, nums):
        return filter(lambda element: element[0] + element[1] > element[2], nums)

    def triangleNumberV0(self, nums):  # 可以找出不重复的三角形个数
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(self.judgeTriangle(self.zipNums(self.sortedNums(nums))))

    def uniquePathsV1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))  # m个a和n个b的组合，(m+n)!/m!n!

    def uniquePathsV2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = [1] * min(m, n)
        t = max(m, n)
        l = len(num)
        for i in range(t - 1):
            for j in range(1, l):
                num[j] += num[j - 1]
        return num.pop()

    def findMinV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: min(x, y), nums)

    def findMinV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            # if the middle is bigger than last val, smallest is on right side
            if nums[mid] > nums[right]:
                left = mid + 1
            # else it could be the curr index or to the left
            else:
                right = mid
        return nums[left]

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # unordered_map < int, int > hash;
        # hash[0] = 1;
        #
        # int sum = 0;
        # int count = 0;
        # for (int i = 0; i < nums.size(); i++){
        #     sum += nums[i];
        #     if (hash.find(sum - k) != hash.end()) count += hash[sum -k];
        #         hash[sum]++;
        # }
        # return count;
        subarray_sum, cumulative_sum, res = {0: 1}, 0, 0
        for index, value in enumerate(nums):
            cumulative_sum += value
            print cumulative_sum, subarray_sum, cumulative_sum - k
            if cumulative_sum not in subarray_sum.keys():
                subarray_sum[cumulative_sum] = index
            else:
                subarray_sum[cumulative_sum] += 1
            if cumulative_sum - k in subarray_sum.keys():
                res += subarray_sum[cumulative_sum - k]
            # if cumulative_sum not in subarray_sum.keys():
            #     subarray_sum[cumulative_sum] = 1
            # print subarray_sum, cumulative_sum - k, res
            # if cumulative_sum == k:
            #     res = index + 1
            # elif cumulative_sum - k in subarray_sum.keys():
            #     res = max(res, index - subarray_sum[cumulative_sum - k])
            # print index - subarray_sum[cumulative_sum - k], "----------"
        return res

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = list(str(num))
        index = 0
        for value in str_num:
            max_number = filter(lambda x: str_num[x] == max(str_num[index:]) and x > index and str_num[x] > value, range(len(str_num)))
            if len(max_number) == 0:
                index += 1
                continue
            else:
                str_num[index], str_num[max_number[-1]] = str_num[max_number[-1]], str_num[index]
                return int("".join(str_num))
        return num

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for value in nums:
            count[value] += 1
        index = 0
        for key in count.keys():
            count2 = 0
            while count2 < count[key]:
                nums[index] = key
                count2 += 1
                index += 1

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid)
        dp[0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i] = dp[i - 1] + grid[i][0]
        for j in range(1, len(grid[0])):
            for i in range(len(grid)):
                dp[i] = min(dp[i], dp[i - 1]) + grid[i][j] if i > 0 else dp[i] + grid[i][j]
        return dp[len(grid) - 1]

    def climbStairsV1(self, n):  # 递归
        """
        :type n: int
        :rtype: int
        """
        res = []
        if n <= 1:
            return 1
        res.extend([1, 1])
        for i in range(2, n + 1):
            res.append(res[-1] + res[-2])
        return res[-1]

    def climbStairsV2(self, n):  # 迭代
        onestep, twostep = 1, 1
        while n > 0:
            twostep += onestep
            onestep = twostep - onestep
            n -= 1
        return onestep

    def robV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a += nums[i]
                a = max(a, b)
            else:
                b += nums[i]
                b = max(a, b)
        return max(a, b)

    def robV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)
        prev, curr = 0, 0
        for i in range(len(nums)):
            print prev + nums[i]
            prev, curr = curr, max(prev + nums[i], curr)
        return curr

    def countBitsV1(self, num):  # Time Limit Exceeded
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num + 1):
            each_number = 0
            for j in range(num):
                if i & 1 << j:
                    each_number += 1
            result.append(each_number)
        return result

    def countBitsV2(self, num):
        re = [0] * (num + 1)
        for i in range(1, num + 1):
            re[i] = re[i & (i - 1)] + 1
        return re

    def countBitsV3(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        k = 0
        while 2**k <= num:
            print [n + 1 for n in result]
            result += [n + 1 for n in result]
            k += 1
        return result[:num+1]



class NumArrayV1(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums is None:
            self.sums = None
        elif len(nums) == 0:
            self.sums = []
        else:
            self.sums = [0] * len(nums)
        for i in range(len(nums)):
            self.sums[i] = self.sums[i - 1] + nums[i]
            print nums[i], self.sums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sums = self.sums
        print sums
        if sums is None:
            return 0
        if i >= len(sums) or j >= len(sums) or i > j:
            return 0
        elif i == 0:
            return sums[j]
        else:
            return sums[j] - sums[i - 1]

class NumArrayV2(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]

if __name__ == '__main__':
    s = Solution()
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]) )
    obj = NumArrayV2([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sumRange(2, 5)
    print(s.countBitsV3(2))














