# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
def lengthOfLongestSubstring(s):
    char_set = set()
    i, max_length = 0, 0
    for j in range(len(s)):
        while s[j] in char_set:
            char_set.remove(s[i])
            i += 1
        char_set.add(s[j])
        max_length = max(max_length, j - i + 1)

    return max_length
