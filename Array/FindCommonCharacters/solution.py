from typing import List
from collections import Counter


def commonChars(A: List[str]) -> List[str]:
    # count first word characters
    firstWordCount = dict(Counter(A[0]))
    # count each word's characters
    for word in A[1:]:
        wordCount = dict(Counter(word))
        # take the min or zero to find intersection
        for ch in firstWordCount:
            firstWordCount[ch] = min(firstWordCount[ch], wordCount.get(ch, 0))

    # the first character counter should only contain # of overlapping characters now
    # convert it to list
    result = list()
    for char, count in firstWordCount.items():
        if count > 0:
            result.extend([char for i in range(count)])
    return result


# test driver
input = ["bella", "label", "roller"]
print("Input:", input)
print("Output:", commonChars(input))

input = ["cool", "lock", "cook"]
print("Input:", input)
print("Output:", commonChars(input))
