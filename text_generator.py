import nltk
from nltk.tokenize import WhitespaceTokenizer
import random

name = input()
file = open(name, "r", encoding="utf-8")
text = file.read()
file.close()
tokens = WhitespaceTokenizer().tokenize(text)
tg = list(nltk.ngrams(tokens, 3))

dict_words = {}
for trio in tg:
    dict_words.setdefault(trio[0] + ' ' + trio[1], {})
    dict_words[trio[0] + ' ' + trio[1]].setdefault(trio[2], 0)
    dict_words[trio[0] + ' ' + trio[1]][trio[2]] += 1

first = [x for x in dict_words if (x[0][0].isupper() and x.split()[0][-1] not in ['.', '!', '?', ','])]

for _ in range(0, 10):
    word = random.choice(first)
    phrase = ""
    phrase += word
    word_next = word
    while True:
        if ((word_next[-1] == '.') or (word_next[-1] == '!') or (word_next[-1] == '?')) and len(phrase.split()) >= 5:
            break
        else:
            word_next = \
                random.choices(list(dict_words[word_next].keys()), weights=list(dict_words[word_next].values()), k=1)[0]
            phrase += " " + word_next
            word_next = phrase.split()[-2] + ' ' + word_next
    print(phrase)
