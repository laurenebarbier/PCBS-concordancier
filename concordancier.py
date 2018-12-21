# Time-stamp: <2018-12-07 14:55>
# Projet de concordancier multilingue
"""Ce programme permet de renvoyer, dans un tableau, à un utilisateur qui cherche un mot dans une langue source
(le français), la traduction, ou les différentes traductions possibles dans une langue cible,
choisie au préalable (anglais ou japonais). L'intérêt d'un concordancier étant qu'il renvoie
également une phrase avec le mot recherché en contexte à partir d'un texte."""

"""Doit créer un outil pour le traitement du texte (division en phrase), et un outil pour """

import pandas as pd
import string

# Permet de choisir la langue cible (langue dans laquelle on veut obtenir une traduction)
print('Choisissez une langue (anglais/japonais)')
target_language = input()
if target_language == 'anglais':
    # Permet d'entrer un mot à chercher
    print('Entrez un mot')
    source_word = input()
    def wordtranslation_english: #si pas possible de mettre une fonction dans une boucle if, mettre output dans une variable et renvoyer résultat
if target_language == 'japonais':
    print('Entrez un mot')
    source_word = input()
    def wordtranslation_japanese:



def wordtranslation_english():
    """Fonction qui permet de renvoyer la traduction et son contexte pour l'anglais"""
    """Doit d'abord rechercher le mot (langue source) dans le fichier terminologie, ensuite
    rechercher le mot (langue cible dans le fichier texte)"""
filename = 'terminologie.txt'
f = open(filename, 'r', encoding='utf-8')
for line in f:
    if source_word in line:
        print(line, end='') """Doit renvoyer tableau avec traduction et une ligne du texte """


def wordtranslation_japanese():
    """Fonction qui permet de renvoyer la traduction et son contexte pour le japonais"""


#corps du programme
if __name__ == '__main__':
        main()

target_text = open('x.txt').read().lower()
text = remove_punctuation(target_text)
sentence = text.split()
print(sentence)
