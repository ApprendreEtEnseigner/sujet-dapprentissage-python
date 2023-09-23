-------------------------------------
1 Observations & Logique
-------------------------------------                       

Entree: /home/../../tmp/.

Entree                      Logique                     Simulation

/                           start                   stack = []
/home                       home                    stack = ["home"]
/                          <= ..                  stack = []
/                          <= ..                 stack = [] (use structures de controle)
tmp                        tmp =>                   stack =["tmp"]
.                           /tmp                    stack =["tmp"]

-----------------------------En python (implementation)--------------------------------------------
start                   initialisation              stack = []
dir                     = 1 pas en avant ( ->)           stack.append(name)
..                      = 1 pas en arriere ( <-)        stack.pop()
.                       ne rien faire        

-------------------------------------
2 Optimized solution
-------------------------------------      