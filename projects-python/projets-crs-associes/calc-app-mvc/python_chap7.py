# De plus, il est recommandé d’utiliser un bloc try-except pour gérer les exceptions qui peuvent se produire lors de l’ouverture d’un fichier, comme un IOError si le fichier n’existe pas ou n’est pas accessible23. Vous pouvez également utiliser l’instruction with pour fermer automatiquement le fichier après avoir terminé de le lire23. Par exemple:

# try: with open(“letter.txt”) as fhand: for line in fhand: if line.startswith(“myBla”): print(line) except IOError as ioe: print(“Erreur lors de l’ouverture du fichier:”, ioe)

fhand = open("letter.txt")
for line in fhand:
    if line.startswith("myBla"):
        print(line)