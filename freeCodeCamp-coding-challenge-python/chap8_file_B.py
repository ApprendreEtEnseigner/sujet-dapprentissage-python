import os
xfile = open("mbox.txt", 'r')
# inp = xfile.read()
# print(len(inp), '\n')
# print(inp[:2])
# # print(fhand)
cwd = os.getcwd()
print(cwd)

count = 0
# with open("mbox.txt") as f:
for cheese in xfile:
        cheese = cheese.rstrip()  #* pour effacer lignes vides
        if not cheese.startswith('From:'):
            print(cheese)
            count += 1
print(count)
