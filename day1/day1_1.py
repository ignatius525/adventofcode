import sys
string = ""
numbers = []

filename = sys.argv[1]

for line in open(filename, 'r'):
    string += line
numbers = string.split('\n')

print(numbers)
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if (numbers[i] + numbers[j] + numbers[k]) == 2020:
                print(numbers[i]*numbers[j]*numbers[k])
            #else:
                #print("fail") 