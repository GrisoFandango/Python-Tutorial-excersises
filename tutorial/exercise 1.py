from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for x in sentence:
    if x in char_frequency:
        char_frequency[x] += 1
    else:
        char_frequency[x] = 1
# pprint(char_frequency)

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)

print(char_frequency_sorted[0])
