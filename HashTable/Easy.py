# -*- coding: utf-8 -*-
from collections import defaultdict
import heapq


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {"q": 1, "w": 1, "e": 1, "r": 1, "t": 1, "y": 1, "u": 1, "i": 1, "o": 1, "p": 1,
                    "a": 2, "s": 2, "d": 2, "f": 2, "g": 2, "h": 2, "j": 2, "k": 2, "l": 2,
                    "z": 3, "x": 3, "c": 3, "v": 3, "b": 3, "n": 3, "m": 3,
                    "Q": 1, "W": 1, "E": 1, "R": 1, "T": 1, "Y": 1, "U": 1, "I": 1, "O": 1, "P": 1,
                    "A": 2, "S": 2, "D": 2, "F": 2, "G": 2, "H": 2, "J": 2, "K": 2, "L": 2,
                    "Z": 3, "X": 3, "C": 3, "V": 3, "B": 3, "N": 3, "M": 3}
        one_row_word = []
        for word in words:
            re = map(lambda x: keyboard[x], word)
            if len(list(set(re))) == 1:
                one_row_word.append(word)
        return one_row_word

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) / 2)

    def groupAnagramsV1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        re, output = {}, []
        for string in strs:
            key = "".join(sorted(string))
            re[key] = re.get(key, [])  # 应该先get再append，否则如果不存在该键就会出错
            re[key].append(string)
        for value in re.values():
            output.append(value)
        return output

    def groupAnagramsV2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        res = []
        for string in strs:
            formatted = ''.join(sorted(string))
            if formatted not in store:
                store[formatted] = len(res)
                res.append([string])
            else:
                res[store[formatted]].append(string)
        return res

    def isAnagramV1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagramV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        默认字典,是字典的一个子类,继承有字典的方法和属性,
        默认字典在进行定义初始化的时候可以指定字典值得默认类型,
        例如字典中没有key = 2，执行dic[2]依然可以返回结果0.
        """
        histogram = defaultdict(int)
        for char in s:
            histogram[char] += 1
        for char in t:
            histogram[char] -= 1

        differences = sum([abs(histogram[x]) for x in histogram])
        return differences == 0

    def findTheDifferenceV1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        histogram = defaultdict(int)
        for char in s:
            histogram[char] += 1
        for char in t:
            histogram[char] -= 1
        for key in histogram.keys():
            if histogram[key] != 0:
                return key

    def findTheDifferenceV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return t

        """
        ord()函数主要用来返回对应字符的ascii码，
        chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。
        """
        result = ord(s[0]) ^ ord(t[0])
        for i in xrange(1, len(s)):
            result ^= ord(s[i]) ^ ord(t[i])

        return chr(result ^ ord(t[-1]))

    def intersectionV1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        letters, re = set(nums1), set()
        for string in nums2:
            if string in letters:
                re.add(string)
        return list(re)

    def intersectionV2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersectionV2(nums2, nums1)  # 始终遍历较长的一个数组
        nums1Set = set(nums1)
        res = []
        for num2 in nums2:
            if num2 in nums1Set:
                res.append(num2)
                nums1Set.discard(num2)  # 如果存在元素，就删除；没有不报异常
        return res

    def frequencySortV1(self, s):
        """
        :type s: str
        :rtype: str
        """
        histogram = defaultdict(int)
        for char in s:
            histogram[char] += 1
        dic = sorted(histogram.items(), key=lambda d: d[1], reverse=True)
        re = ""
        for key, value in dic:
            re += key * value
        return re

    def frequencySortV2(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_map = {c: s.count(c) for c in set(s)}  # 字符串的count方法更方便

        # convert to list to sorted by count
        by_freq = sorted([(v, k) for k, v in freq_map.items()], reverse=True)

        # turn list of tuples into output string
        output = [t[1] * t[0] for t in by_freq]

        return ''.join(output)

    def topKFrequentV1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        histogram = defaultdict(int)
        re = []
        for char in nums:
            histogram[char] += 1
        dic = sorted(histogram.items(), key=lambda d: d[1], reverse=True)
        for i in range(k):
            re.append(dic[i][0])
        return re

    def topKFrequentV2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        元素计数
        """
        num_count = defaultdict(int)
        for x in nums:
            num_count[x] += 1

        heap = []
        for num, count in num_count.iteritems():
            pair = (-count, num)
            heapq.heappush(heap, pair)

        result = []
        for _ in xrange(k):
            num = heapq.heappop(heap)[1]
            result.append(num)
        return result

    def topKFrequentWordV1(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        histogram = defaultdict(int)
        re = []
        for word in words:
            histogram[word] += 1
        """
        如果想对更多的key进行排序（不只是两个），例如对l = [(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 2, 5)]
        这样的数组，先比最后一个，再比倒数第二个，最后比第一个只需在lambda表达式处返回相应元组即可：
        sorted(l, key=lambda x: (x[3], x[2], x[1], x[0])),要对某个key逆序，则再前面加“-”,
        但只限于数字类型，字符串类型不支持
        """
        dic = sorted(histogram.items(), key=lambda d: (-d[1], d[0]))  # 这步可直接排好序的取前k个，然后用列表推导式输出
        for i in range(k):
            re.append(dic[i][0])
        return re

    def topKFrequentWordV2(self, words, k):
        counts = {}
        for w in words:
            if w in counts:
                counts[w] += 1
            else:
                counts[w] = 1
        ans = sorted(counts.items(), key=lambda i: (-i[1], i[0]))[:k]
        return [x[0] for x in ans]

    def findLHSV1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        histogram = defaultdict(int)
        for num in nums:
            histogram[num] += 1
        dic, re = sorted(histogram.items(), key=lambda d: d[0]), 0
        for index in range(len(dic) - 1):
            if abs(dic[index][0] - dic[index + 1][0]) == 1:
                re = max(re, dic[index][1] + dic[index + 1][1])
        return re

    def findLHSV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dic = {}
        target = 0
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        """
        没有排序一步，并且是直接从字典中取值，没有元组，有可能因为字典的键值插入就是有序的
        """
        for k in dic.keys():
            if k - 1 in dic:
                target = max(target, dic[k] + dic[k - 1])

        return target

    def isIsomorphicV1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sourceMap, targetMap = dict(), dict()
        for x in range(len(s)):
            source, target = sourceMap.get(t[x]), targetMap.get(s[x])
            if source is None and target is None:
                sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:
                return False
        return True

    def isIsomorphicV2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print set(zip(s, t)), zip(s, t)
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphicV3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        replace_map = {}
        for i in range(len(s)):
            if s[i] not in replace_map:
                replace_map[s[i]] = t[i]
            else:
                if replace_map[s[i]] != t[i]:
                    return False

        values = replace_map.values()
        return len(set(values)) == len(values)

    def countPrimesV1(self, n):  # Memory Limit Exceeded
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        if n <= 2:
            return 0
        for i in range(2, n):
            dic[i] = True
        for key in dic.keys():
            if dic[key] is True:
                times = 2
                while key * times < n:
                    if dic[key * times] is True:
                        dic[key * times] = False
                    times += 1
        return len(filter(lambda x: dic[x] is True, dic))

    def countPrimesV2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        number_type, count = [True] * n, 0
        for i in range(2, n):
            if number_type[i] is True:
                count += 1
                times = 2
                while i * times < n:
                    if number_type[i * times] is True:
                        number_type[i * times] = False
                    times += 1
        return count

    def wordPattern(self, pattern, string_pattern):
        """
        :type pattern: str
        :type string_pattern: str
        :rtype: bool
        """
        replace_map, pattern_letter = list(pattern), string_pattern.split(' ')
        return len(set(zip(replace_map, pattern_letter))) == len(set(replace_map)) == len(set(pattern_letter)) and len(replace_map) == len(pattern_letter)

    def findAnagramsV1(self, s, p):  # Time Limit Exceeded
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_histogram = defaultdict(int)
        for i in p:
            p_histogram[i] += 1
        length, re = len(p), []
        for i in range(len(s) - length + 1):
            s_histogram = defaultdict(int)
            for j in s[i:i + length]:
                s_histogram[j] += 1
            if s_histogram == p_histogram:
                re.append(i)
        return re

    def findAnagramsV2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) == 0 or len(p) == 0 or len(s) < len(p):
            return []
        p_histogram, s_histogram, length, re = defaultdict(int), defaultdict(int), len(p), []
        for i in range(length):
            p_histogram[p[i]] += 1
            s_histogram[s[i]] += 1
        left, right = 0, 0 + length
        if p_histogram == s_histogram:
            re.append(0)
        while right < len(s):
            s_histogram[s[left]] -= 1
            s_histogram[s[right]] += 1
            if s_histogram[s[left]] == 0:
                del s_histogram[s[left]]
            left += 1
            right += 1
            if p_histogram == s_histogram:
                re.append(left)
        return re

    def checkInclusionV1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) == 0 or len(s2) == 0 or len(s1) > len(s2):
            return False
        s1_histogram, s2_histogram, length = defaultdict(int), defaultdict(int), len(s1)
        for i in range(length):
            s1_histogram[s1[i]] += 1
            s2_histogram[s2[i]] += 1
        left, right = 0, 0 + length
        if s1_histogram == s2_histogram:
            return True
        while right < len(s2):
            s2_histogram[s2[left]] -= 1
            s2_histogram[s2[right]] += 1
            if s2_histogram[s2[left]] == 0:
                del s2_histogram[s2[left]]
            left += 1
            right += 1
            if s1_histogram == s2_histogram:
                return True
        return False

    def checkInclusionV2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        r = [0] * 26
        for i in s1:
            print ord(i), ord('a')
            r[ord(i) - ord('a')] += 1

        r1 = [0] * 26
        for i in s2[:len(s1)]:
            r1[ord(i) - ord('a')] += 1
        if r1 == r:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            r1[ord(s2[i - 1]) - ord('a')] -= 1
            r1[ord(s2[i + len(s1) - 1]) - ord('a')] += 1
            if r == r1:
                return True
        return False

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""
        s_histogram, t_histogram, t_length = defaultdict(int), defaultdict(int), len(t)
        for i in range(len(s)):
            s_histogram[s[i]] += 1
            if i < len(t):
                t_histogram[t[i]] += 1
        left, right = 0, len(s) - 1
        while left + t_length < right:
            for key in t_histogram.keys():
                if t_histogram[key] <= s_histogram[key]:
                    s_histogram[s[left]] -= 1
                    left += 1
                else:
                    break
        while left + t_length < right:
            for key in t_histogram.keys():
                if t_histogram[key] <= s_histogram[key]:
                    s_histogram[s[right]] -= 1
                    right += 1
                else:
                    break
        return s[left:right + 1]

    def isHappyV1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1 and n != 4:
            t = 0
            while n:
                t += (n % 10) * (n % 10)
                n /= 10
            n = t
        return n == 1

    def isHappyV2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 0
        count = 0
        m = []
        while n != 1:
            if n in m:
                return False
            m.append(n)
            temp = n % 10
            while n >= 10:
                count += temp * temp
                n = n // 10
                temp = n % 10
            count += n * n
            n = count
            count = 0
            temp = 0
        return True

    def longestPalindromeV1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s_histogram, length, count = defaultdict(int), 0, 0
        for string in s:
            s_histogram[string] += 1
        for num in sorted(s_histogram.values(), reverse=True):
            if num % 2 == 0:
                length += num
            elif count == 0:
                length += num
                count += 1
            else:
                length += num - 1
        return length

    def longestPalindromeV2(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = set(s)
        sum = 0
        odd = 0
        for i in p:
            k = s.count(i)
            if k % 2 == 0:
               sum = sum + k
            else:
               odd = odd + 1
               sum = sum + k
        if odd == 0:
            return sum
        else:
            return sum - (odd-1)  # 有odd个奇数，只要最后给odd-1个奇数减1即可

    def intersectV1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_histogram, nums2_histogram, nums1_length, nums2_length, re = \
            defaultdict(int), defaultdict(int), len(nums1), len(nums2), []
        for index in range(max(nums1_length, nums2_length)):
            if index < nums1_length:
                nums1_histogram[nums1[index]] += 1
            if index < nums2_length:
                nums2_histogram[nums2[index]] += 1
        if len(nums1_histogram) > len(nums2_histogram):
            traversal_dict = nums2_histogram
            search_dict = nums1_histogram
        else:
            traversal_dict = nums1_histogram
            search_dict = nums2_histogram
        print traversal_dict, '\n', search_dict
        for key in traversal_dict.keys():
            if key in search_dict:
                re += [key] * min(search_dict[key], traversal_dict[key])
        return re

    def intersectV2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # a,b = map(collections.Counter, (nums1,nums2))
        # return list((a & b).elements())

        result = []
        count = {}
        for num in nums2:
            count[num] = count.get(num, 0) + 1

        for num in nums1:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    #print(s.getRowV2(3))
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]))
    print(s.intersectV1([1], []))
