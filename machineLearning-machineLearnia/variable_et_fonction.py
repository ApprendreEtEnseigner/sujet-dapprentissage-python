
# fhand = open('mbox.txt', 'r')
# print(fhand)

def e_potentielle(masse, hauteur, e_limite, g):
    E = masse * hauteur * g
    print(E, 'Joules')
    
    return E

e_potentielle(masse=80, hauteur=1.5, e_limite=9.81)
    
