# https://leetcode.com/discuss/interview-question/4024498/IBM-Software-Developer-2023-2024-(Full-Time)-HackerRank
def getMinFlips(s):
    flips = 0
    for i in range(0, len(s) - 1, 2):
        if s[i] != s[i + 1]:
            flips += 1
    print("Minimum flips required: ", flips)


# s = '1110011000'
s = '101011'
getMinFlips(s)
