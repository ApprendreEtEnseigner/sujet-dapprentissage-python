
# fhand = open('mbox.txt', 'r')
# print(fhand)

with open("mbox.txt", 'r') as f:
    for line in f:
        print(line)
