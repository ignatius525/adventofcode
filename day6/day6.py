import sys
string = ""
numbers = []
answers = []
letters = []

sums = 0

filename = sys.argv[1]

for line in open(filename, 'r'):
    string += line
numbers = string.split('\n\n')

for i in range(len(numbers)):
    numbers[i] = numbers[i].replace("\n", " ")

#print(numbers)

for i in range(len(numbers)):
    res = numbers[i].split(" ")
    answers.append(res)

#print(answers)

#for i in range(26):
    #letters.append(0)

#print(letters)

for x in answers:
    letters = []
    #for k in range(26):
        #letters.append(0)
    for i in range(len(x)):
        y = []
        for k in range(26):
            y.append(0)
        for j in range(len(x[i])):
            val = ord(x[i][j:j+1]) - 97
            y[val] = 1
        letters.append(y)
        print(letters)
    foo = []
    for a in range(26):
        foo.append(0)
    for f in range(len(letters)):
        check = len(letters)
        for b in range(len(letters[f])):
            if letters[f][b] == 1:
                foo[b] = foo[b] + 1
        for c in range(len(foo)):
            if foo[c] == check:
                sums += 1

        #if letters[f] == 1:
            #sums += 1
print(sums)

                
