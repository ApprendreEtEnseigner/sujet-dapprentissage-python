
# !---------------------------------SCRIPT---------------------------------------------------
# ? Considérons que tu as plus de 10 ans d'expérience en programation avec python. Moi je suis un jeune de 12 ans, apprenant à coder. Explique étape par étape, le code ci dessous, en utilisant des exemples simples pour me permettre de comprendre:

# !---------------------------------v1----------------------------------------------------
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

# !---------------------------------v2----------------------------------------------------
def narcissistic( value ):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)

print(narcissistic(152))

# !---------------------------------v3----------------------------------------------------
def narcissistic(value):
    return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))

# !---------------------------------v4----------------------------------------------------
narcissistic = lambda n: sum([int(d) ** len(str(n)) for d in list(str(n))]) == n

# !---------------------------------v5----------------------------------------------------
def narcissistic( value ):
    v = value
    l = len(str(value))
    s = 0
    while v > 0:
        s += (v % 10)**l
        v //= 10

    return s == value

# !---------------------------------v6----------------------------------------------------
def narcissistic( value ):
    s = str(value)
    return sum(map(lambda x: int(x) ** len(s), s)) == value 