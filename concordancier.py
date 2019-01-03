# Time-stamp: <2018-12-07 14:55>
# Projet de concordancier multilingue
"""Ce programme permet de renvoyer, dans un tableau, à un utilisateur qui cherche un mot dans une langue source
(le français), la traduction, ou les différentes traductions possibles dans une langue cible,
choisie au préalable (anglais ou japonais). L'intérêt d'un concordancier étant qu'il renvoie
également une phrase avec le mot recherché en contexte à partir d'un texte."""


import pandas as pd
import string

# Permet de choisir la langue cible (langue dans laquelle on veut obtenir une traduction)
print('Choisissez une langue (anglais/japonais)')
target_language = input()
print('Entrez un mot')
source_word = input()


def word_mapping(f):
        """Fonction qui permet de renvoyer la traduction et son contexte pour l'anglais"""
        """Doit d'abord rechercher le mot (langue source) dans le fichier terminologie, ensuite
        rechercher le mot (langue cible dans le fichier texte)"""
if target_language == 'anglais':
    filename = 'terminologie.txt'
    f = open(filename, 'r', encoding='utf-8')
    table = pd.Series()
    for source_word in items:
        if str(it) in table.index:
            table[str(source_word)] += 1
        else:
            table[str(source_word)] = 1
    return table.sort_values(ascending=False)

    for line in f:
        if source_word in line:
            print(line, end='')

def word_translation():


if target_language == 'japonais':



#corps du programme
if __name__ == '__main__':
        main()
def word_mapping(f):
def word_translation():
sentence =
print(sentence)
