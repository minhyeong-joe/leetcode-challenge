def arrangeWords(text: str) -> str:
    # split into array of words
    words = text.split(" ")
    wordLength = list()
    # count words and sort by word length
    for word in words:
        wordLength.append((word.lower(), len(word)))
    wordLength.sort(key=lambda pair: pair[1])
    # extract words sorted by word length
    words = [w for w,_ in wordLength]
    # join the words and capitalize the first one
    return " ".join(words).capitalize()


# test driver
text = "Leetcode is cool"
print("Input: text = \"" + text + "\"")
print("Output: \"" + arrangeWords(text) + "\"")
print()

text = "Keep calm and code on"
print("Input: text = \"" + text + "\"")
print("Output: \"" + arrangeWords(text) + "\"")
print()

text = "To be or not to be"
print("Input: text = \"" + text + "\"")
print("Output: \"" + arrangeWords(text) + "\"")