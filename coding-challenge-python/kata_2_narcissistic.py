def narcissistic(value):
    # convert number in string 
    value_str = str(value)
    
    # obtenir le nombre de chiffres dans le nombre
    num_digits = len(value_str)
    
    # la variable pour sommer les chiffres
    sum_powered_digits = 0
    
    # parcourir chaque caractere de value_str
    for char in value_str:
        #* Convertir le caractère en un nombre entier
        digit = int(char)
        #* Calculer la puissance du nombre de chiffres pour ce chiffre
        powered_digit = digit ** num_digits
        # Ajouter le résultat à la somme
        sum_powered_digits += powered_digit
    # Comparer la somme avec le nombre original
    if ( sum_powered_digits == value):
        return True
    else:
        return False
        
# print(narcissistic(153))
# print(narcissistic(370))