'''
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


def longestCommonPrefix(self, strs: List[str]) -> str:
    lcp = ""
    target = strs[0]
    for key, val in enumerate(target):
        found = 0
        for i in strs[1:]:
            if key <= len(i)-1:
                if val == i[key]:
                    found += 1
                else:
                    found -= 1
        if found == len(strs[1:]):
            lcp += val
        else:
            break
    return lcp
