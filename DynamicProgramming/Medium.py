# -*- coding: utf-8 -*-
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        定义d[i][j]：若从i到j的字符串为回文，则为真（1），否则为假（0），
        那么d[i][j]为真的前提是：头尾两个字符串相同并且去掉头尾以后的字串也是回文（即d[i+1][j-1]为真），
        这里面要注意特殊情况，即：去掉头尾以后为空串，所以如果j-i>3，并且头尾相等，也是回文的。
        这样就得到了下面的关键代码：dp[i][j]=((s[i]==s[j])&&(j-i<3||dp[i+1][j-1]));
        """
        length, res = len(s), 0
        dp = [[0] * length] * length
        for i in reversed(range(length)):
            for j in range(i, length):
                print dp
                dp[i][j] = ((s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1]))
                if dp[i][j] is True:
                    res += 1
        return res

    def countSubstringsV2(self, input):
        input = '#' + '#'.join(input) + '#'
        RL = [0] * len(input)
        MaxRight = 0
        pos = 0
        MaxLen = 0
        for i in range(len(input)):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            # 尝试扩展，注意处理边界
            while i - RL[i] >= 0 and i + RL[i] < len(input) and input[i - RL[i]] == input[i + RL[i]]:
                RL[i] += 1
            # 更新MaxRight,pos
            if RL[i] + i - 1 > MaxRight:
                MaxRight = RL[i] + i - 1
                pos = i
            # 更新最长回文串的长度
            MaxLen = max(MaxLen, RL[i])
        return MaxLen - 1

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count1 = 0
        for i in range(2, n + 1):
            num, count2, index = i, 1, 0
            while num > 0:
                print num, "+++++++++"
                if num == 1:
                    print index, "=========", count2
                    count2 *= (9 - index + 2)
                else:
                    count2 *= (9 - index)
                    print count2, "--------"
                index += 1
                num -= 1
                count1 += count2
        print count1 + 10





        # for i in range(1, n + 1):
        #     num, count2, count3 = i, 9, 9
        #     while num > 0:
        #
        #         print num, i, "======"
        #         if num == 1:
        #             print 9 - i + 2
        #             count2 *= (9 - i + 2)
        #         else:
        #             count2 *= (9 - num)
        #         num -= 1
        #         count1 += count2



if __name__ == '__main__':
    s = Solution()
    #print(s.removeDuplicatesV2([1, 1, 2, 2, 3]) )
    print(s.countNumbersWithUniqueDigits(2))




