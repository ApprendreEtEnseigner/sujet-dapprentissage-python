
# ! STACK DATA STRUCTURES


#*-------------------------------------------------
#? creata stack
#*-------------------------------------------------

stack = []

#*-------------------------------------------------
#? Operation 1: add     | Identifiant 1: push 
#*-------------------------------------------------
#! ici, add signifie ajouter dans la pile (=stack)
stack.append(3)

#*-------------------------------------------------
#? Operation 2: peek     | Identifiant 2: [-number] 
#*-------------------------------------------------
#! ici, peek signifie celui qui est au sommet de la pile (=stack)
stack[-1]

#*-------------------------------------------------
#? Operation 3: remove    | Identifiant 3: pop
#*-------------------------------------------------
#! ici, remove signifie sortir de la pile (=stack)
stack.pop()

#*-------------------------------------------------
#? Operation 4: is_exist    | Identifiant 3: stack
#*-------------------------------------------------
#! ici, is_existe signifie si la pile (=stack) est vide ou non
is_empty = stack == ""
print(is_empty)