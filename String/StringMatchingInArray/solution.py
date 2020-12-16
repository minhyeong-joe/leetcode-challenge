from typing import List

def stringMatching(words: List[str]) -> List[str]:
    substrings = list()
    words.sort(key=lambda w: len(w))
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # if words[i] is substring of words[j], insert to substring and exit current loop
            if words[i] in words[j]:
                substrings.append(words[i])
                break
    return substrings



# test driver
words = ["mass","as","hero","superhero"]
print("Input: words =", words)
print("Output:", stringMatching(words))
print()

words = ["leetcode","et","code"]
print("Input: words =", words)
print("Output:", stringMatching(words))
print()

words = ["blue","green","bu"]
print("Input: words =", words)
print("Output:", stringMatching(words))
print()