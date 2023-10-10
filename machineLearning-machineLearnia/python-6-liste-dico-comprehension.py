
#* On peut...
    

# ! On ne peut pas...
    
    

# ! CORRECTION F(X) TRIER

classeur = {
    "positif": [],
    'negatif': []
}
def trier(classeur,nombre):
    if nombre > 0:
        is_positif = classeur['positif'].append(nombre)
    elif ( nombre < 0 ):
        is_negatif = classeur['negatif'].append(nombre)
    else:
        print('Erreur')
    
    return classeur 
        
print(trier(classeur, 3))
