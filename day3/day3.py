import sys
string = ""
numbers = []
posright = 0
treecount1 = 0
treecount2 = 0
treecount3 = 0
treecount4 = 0
treecount5 = 0
filename = sys.argv[1]

for line in open(filename, 'r'):
    string += line
numbers = string.split('\n')

#print(numbers)

#print(len(numbers[0]))

#print(len(numbers))

for i in range(1, len(numbers)):
    posright += 3
    if posright > 30:
        posright = posright % 31
    if (numbers[i][posright] == '#'):
        treecount2 += 1

print(treecount2)
posright = 0

for i in range(1, len(numbers)):
    posright += 1
    if posright > 30:
        posright = posright % 31
    if (numbers[i][posright] == '#'):
        treecount1 += 1

print(treecount1)

posright = 0

for i in range(1, len(numbers)):
    posright += 5
    if posright > 30:
        posright = posright % 31
    if (numbers[i][posright] == '#'):
        treecount3 += 1

print(treecount3)

posright = 0

for i in range(2, len(numbers), 2):
    posright += 1
    if posright > 30:
        posright = posright % 31
    if (numbers[i][posright] == '#'):
        treecount4 += 1

print(treecount4)

posright = 0

for i in range(1, len(numbers)):
    posright += 7
    if posright > 30:
        posright = posright % 31
    if (numbers[i][posright] == '#'):
        treecount5 += 1

print(treecount5)

sums = treecount1 * treecount2 * treecount3 * treecount4 *treecount5

print(sums)