'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
'''
from collections import defaultdict


def findSubstring(s, words):
    # base case
    if not s and not words:
        return []

    # tracking the words
    word_count = defaultdict(int)
    for i in words:
        word_count[i] += 1

    # sliding window, word length, word count, & results
    sliding_window = len(words) * len(words[0])
    word_length = len(words[0])
    result = []

    # initial sliding iteration of the string
    for i in range(len(s) - sliding_window + 1):
        exists = defaultdict(int)
        j = i
        check = 0
        while j < i + sliding_window:
            word = s[j:j + word_length]
            if word in word_count:
                exists[word] += 1
                if exists[word] > word_count[word]:
                    check = -1
                    break
            else:
                check = -1
                break
            j += word_length
        if check == 0:
            result.append(i)
    return result


print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
