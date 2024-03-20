"""Exercise"""

# count most frequent characters sentence
# pretty print (pprint) package to print with formarting
# from pprint import pprint
SENTENCE = "This is a common interview question"
char_frequency = {}
for char in SENTENCE:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)

# lets sort the output

# items() covert key value pair of dictionery into tuple
# the output is not sorted because it is tuple and sorted() don't know
# how to sort a tuple so we sort it based second value of tuple
# in key parameter is the basis on which we sort the values
# pep 8 recommends 80 charactes max per line
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True
)

print(char_frequency_sorted[0])
