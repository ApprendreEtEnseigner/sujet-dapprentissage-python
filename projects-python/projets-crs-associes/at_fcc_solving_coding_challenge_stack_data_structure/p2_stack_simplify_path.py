# def simplify_path(path):
    
#     stack = []
#     for directory in path.split("/"):
#         if directory == "":
#             pass
#         elif directory == ".":
#             pass
#         elif directory == "..":
#             if stack:
#                 stack.pop()
#             else:
#                 pass
#         else:
#             stack.append(directory)
#     return "/" + "/".join(stack)

# print(simplify_path("/home/"))  # Attendu : "/home"
# print(simplify_path("/../"))  # Attendu : "/"
# print(simplify_path("/home//foo/"))  # Attendu : "/home/foo"
# print(simplify_path("/a/./b/../../c/"))  # Attendu : "/c"
# print(simplify_path("/a/../../b/../c//.//"))  # Attendu : "/c"
# print(simplify_path("/a//b////c/d//././/.."))  # Attendu : "/a/b/c"

#! By BingPrecise
# def simplify_path(path):
#     dirs = path.split('/')
#     canonical_path = []
#     for dir in dirs:
#         if dir == "" or dir == ".":
#             continue
#         if dir == "..":
#             if canonical_path:
#                 canonical_path.pop()
#             continue
#         canonical_path.append(dir)
#     result = "/" + "/".join(canonical_path)
#     return result

# print(simplify_path("/home/"))  # Doit afficher "/home"
# print(simplify_path("/../"))  # Doit afficher "/"
# print(simplify_path("/home//foo/"))  # Doit afficher "/home/foo"
# print(simplify_path("/a/./b/../../c/"))  # Doit afficher "/c"

#! By BingCreative
# Définition de la fonction simplify_path qui prend en paramètre une chaîne de caractères path
def simplify_path(path):
    # On vérifie que path est une chaîne de caractères non vide et qu'elle commence par un '/'
    if not isinstance(path, str) or not path or path[0] != '/':
        # Sinon, on lève une exception ValueError avec un message d'erreur
        raise ValueError("path doit être une chaîne de caractères non vide qui commence par un '/'")
    
    # On découpe le chemin en segments en utilisant le séparateur '/'
    segments = path.split('/')
    
    # On initialise une liste vide pour représenter une pile
    stack = []
    
    # On parcourt les segments du chemin avec une boucle for
    for segment in segments:
        # Si le segment est vide ou égal à '.', on l'ignore
        if segment == '' or segment == '.':
            continue
        # Si le segment est égal à '..', on dépile le dernier segment ajouté à la pile, s'il existe
        elif segment == '..':
            if stack:
                stack.pop()
        # Sinon, on empile le segment dans la pile
        else:
            stack.append(segment)
    
    # On joint les segments de la pile avec le séparateur '/' et on ajoute un '/' au début
    canonical_path = '/' + '/'.join(stack)
    
    # On retourne le chemin canonique simplifié
    return canonical_path

# Exemples pour tester la fonction

# Exemple 1: chemin valide avec des répertoires et des fichiers
path = '/home/user/Documents/file.txt'
print(simplify_path(path)) # affiche '/home/user/Documents/file.txt'

# Exemple 2: chemin valide avec des points et des doubles points
path = '/a/./b/../../c/'
print(simplify_path(path)) # affiche '/c'

# Exemple 3: chemin valide avec des points et des doubles points au début et à la fin
path = '/../a/b/c/..'
print(simplify_path(path)) # affiche '/a/b'

# Exemple 4: chemin invalide qui ne commence pas par un '/'
path = 'a/b/c'
print(simplify_path(path)) # lève une exception ValueError

# Exemple 5: chemin invalide qui n'est pas une chaîne de caractères

path = 123
print(simplify_path(path)) # lève une exception ValueError


