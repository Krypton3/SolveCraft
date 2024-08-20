'''
Consider a string, S, that is a series of characters, each followed by its
frequency as an integer. The string is not compressed correctly, so there may
be multiple occurrences of the same character. A properly compressed string
will consist of one instance of each character in alphabetical order followed
by the total count of that character within the string.
'''


def compress_string(value):
    keep = []
    size = len(value)
    result = ""
    i = 0
    while i < size:
        if i % 2 != 0:
            char = value[i - 1]
            number = int(value[i])
            if char not in keep:
                keep.append(char)
                result = result + (char * number)
        i = i + 1
    return result


print("The compressed string is: ", compress_string("a3b5c2a2"))
