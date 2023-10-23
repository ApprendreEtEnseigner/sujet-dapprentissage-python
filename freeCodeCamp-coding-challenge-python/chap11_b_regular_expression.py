
import re 


#! CARACTERS SPECIAUX ET SIGNIFICATIONS:
    # [0-9] => retourne 1 chiffre entre 1-9
    # [0-9]+ => retourne 1 ou plusieurs chiffres entre 1-9

#! ici, nous usons une methode ( findall() ) pour retourner une liste respectant le model donnee. 
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
#! s'il ne trouve rien, il renvoie une liste vide. nb ca ne retourne pas faux
y = re.findall('[AEIOU]+', x)
print(y)

letter = 'From: using the: character'
#!  S'il ya +sieurs : dans le model, on s'arrete au dernier  (ie; format long)
z = re.findall("^F.+:", letter)
print(z)
#!  Pour s'arreter au premier : on use ? dans le model (ie: format court)
z = re.findall("^F.+?:", letter)
print(z)
