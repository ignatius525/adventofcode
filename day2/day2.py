import sys
string = ""
passwords = []
totalpass = 0
filename = sys.argv[1]

for line in open(filename, 'r'):
    string += line
passwords = string.split('\n')

#print(passwords)

line = []

lst = []

for i in range(len(passwords)):
    line = passwords[i].split(' ')
    lst.append(line)
    #print(line)

#print(lst)

for i in range(len(lst)):
    lst[i][1] = lst[i][1][:1]

#print(lst)

for i in range(len(lst)):
    lst[i][0] = lst[i][0].split("-")
    for j in range(len(lst[i][0])):
        lst[i][0][j] = int(lst[i][0][j])

#print(lst)

for i in range(len(lst)):
    print(lst[i])

for i in range(len(lst)):
    #count = 0
    boofirst = False
    boosecond = False
    firstpos = lst[i][0][0] - 1
    secondpos = lst[i][0][1] - 1
    #print(minimum, " ", maximum)
    char = lst[i][1]
    #print(char)
    #count = lst[i][2].count(char)
    #print(count)
    #if (count >= minimum) and (count <= maximum):
        #totalpass+=1
    if lst[i][2][firstpos:firstpos+1] == (char):
        boofirst = True
    if lst[i][2][secondpos:secondpos+1] == (char):
        boosecond = True
    
    if (boofirst == True) or (boosecond == True):
        if(boofirst == True) and (boosecond == True):
            continue
        else:
            totalpass +=1
    print(totalpass)  
        