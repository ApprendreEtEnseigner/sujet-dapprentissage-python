
def fib(n):
    a = 0
    b = 1
    list_fib = []
    while a < n:
        print(a)
        a, b = b, a+b
        print(list_fib.append(a))
        
        
print(fib(2))