# Time-stamp: <2018-12-07 14:55>
# Projet de concordancier multilingue
""

import pandas as pd
import string

#enlève la ponctuation du texte utilisé
def remove_punctuation(text):
    punct = string.punctuation + chr(10)
    return text.translate(str.maketrans(punct, " " * len(punct)))

#recherche une chaine de caractère
STRING = 'x'
FILENAME = 'x'
f = open(FILENAME, 'r', encoding='utf-8')
for line in f:
    if STRING in line:
        print(line, end='')


#corps du programme
if __name__ == '__main__':
        main()

textori = open('alice.txt').read().lower()
text = remove_punctuation(textori)
words = text.split()
print(words)
