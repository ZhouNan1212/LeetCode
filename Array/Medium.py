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




if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.combinationSum3(4, 10))
