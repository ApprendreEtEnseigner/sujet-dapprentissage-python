
# Principe ? faire des recherches intelligentes
# c'est un langage de programmation, mais base sur des caracters et pas sur des lignes.
# lien utile ? xkcd.com/208/ 
# info annexe ? 
# - norme educative: Learning Tools Interoperabillity
# - plateforme: Coursera, Blackboard, Canvas, Sakai, Moodle

# NB: les reg exp ne font pas parti du python de base, il faut importer la biblio (re)

import re 

#! ici, nous programmons une re. ie: nous manquons de methodes dqns la class string pour tous les besoins
# with open('mbox.txt', 'r') as hand:
#     for line in hand:
#         line = line.rstrip()
#         if re.search('From', line):
#             print(line)

#! CARACTERS SPECIAUX ET SIGNIFICATIONS:
    # ^ => debut de la ligne
    # . => nimporte quel caractere
    # * => pour modifier le caractere qui precede immediatement le caracter en cours.
    # \ => tout caract autre qu'un espace blanc.
    # + => une ou plusieurs fois la regple precedant le +
    #  () => indique le debut et la fin de l'extraction

# - Espace blanc : un espace blanc est un caractère invisible utilisé pour la mise en forme du texte. Il peut s'agir d'un espace, d'une tabulation, d'un retour à la ligne, etc.
# - \S : cette expression régulière correspond à tout caractère qui n'est pas un espace blanc.
# - \s : cette expression régulière correspond à un espace blanc.
# - . : ce point représente n'importe quel caractère, y compris les espaces blancs.
# - _ : ce caractère souligné ne correspond à rien en particulier dans le contexte des expressions régulières.
# - \. : cette expression régulière correspond à un point (.) littéral.

    

#! ici, nous usons une methode ( startswith() )la ligne commence a partir de From (via  startswith() ), ie: ici la limite, c'est vtre imgination

with open('mbox.txt', 'r') as hand:
    for line in hand:
        line = line.rstrip()
        if line.startswith('From'):
            print(line)
            
            
# ------------------------------------- QUIZ -------------------------------------------------------
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)


#1 ['csev@umich.edu', 'cwen@iupui.edu']

#2 ['csev@umich.edu']

#3 ['umich.edu', 'iupui.edu']

#4 ['csev@', 'cwen@']

# Ce code est écrit en Python et utilise le module `re` (pour "regular expressions" ou expressions régulières) pour trouver toutes les adresses email dans une chaîne de caractères donnée.

# La chaîne de caractères `s` contient un message avec deux adresses email : 'csev@umich.edu' et 'cwen@iupui.edu'. Le code utilise la fonction `re.findall(pattern, string)` pour trouver toutes les occurrences d'un motif (pattern) dans une chaîne de caractères (string).

# Le motif utilisé est '\\S+@\\S+', qui correspond à une séquence de caractères non-blancs (\\S+) suivie d'un symbole '@' et d'une autre séquence de caractères non-blancs (\\S+). 

# La fonction `re.findall()` renvoie une liste contenant toutes les occurrences trouvées. Dans ce cas, la liste renvoyée est ['csev@umich.edu', 'cwen@iupui.edu'].

# Les autres lignes de code ne sont pas nécessaires pour comprendre le fonctionnement de la recherche d'adresses email.