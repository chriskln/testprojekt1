import re
import string

frequency = { }

basis_text = open("wordcount.txt", "r")
string_text = basis_text.read().lower()
total_text = re.findall(r"\b[a-z]{1,100}\b", string_text)

for word in total_text:
    count = frequency.get(word,0)
    frequency[word] = count + 1

list_frequency = frequency.keys()
for words in list_frequency:
    print(words, frequency[words])



