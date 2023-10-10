
#* On peut...
    #  nester les dico
    

# ! On ne peut pas...
    # avoir menme cle pour +sieurs values
    

# ! CORRECTION F(X) FIBONACI
def fib(n):
    #  retourner une liste contenant la suite de fibonaci jusqu'a n
    a = 0
    b = 1
    list_fib = [a]
    while a < n:
        print(a)
        a, b = b, a+b
    return list_fib.append(a)
        
        
print(fib(1000))