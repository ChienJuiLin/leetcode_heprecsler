'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        t=len(strs)

        ans,i,corr,x = '',0,False,1

        if t == 1: return strs[0]
        elif t == 0 or '' in strs: return ''

        minStringIndex = strs.index(min(strs, key=len))
        strs[0],strs[minStringIndex] = strs[minStringIndex],strs[0]

        while True:
            newC = strs[0][i]
            while x <= t-1:
                if newC != strs[x][i]:
                    corr = True
                    break
                x += 1
            if corr: break
            x = 1
            ans = ans + newC
            i += 1
            if i >= len(strs[0]): break

        return ans

# 這字串處理真的很漂亮
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ("")
        length = min(strs, key=len)
        strs.remove(length)
'''
# 尤其是這個部分，直接把最短字的每個字母編號，再逐一和其他各String的各個字母比較
# 如果字母一不相等，就回傳前所有比對過的部分
'''
        for i, x in enumerate(length):
            for item in strs:
                if item[i] != x:
                    return(length[:i])
        return(length)
'''
