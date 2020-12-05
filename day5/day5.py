import sys
string = ""
numbers = []
highest = 0
lowest = 9999999
seats= []
for i in range(872):
    seats.append(0)

filename = sys.argv[1]

for line in open(filename, 'r'):
    string += line
numbers = string.split('\n')

print(numbers)

for x in numbers:
    final = 0
    array = []
    columns = [0,1,2,3,4,5,6,7]
    for i in range(128):
        array.append(i)
    for k in range(7):
        f = x[k:k+1]
        if f == "F":
            array = array[:int(len(array)/2)]
        else:
            array = array[int(len(array)/2):]
    for j in range(7,10):
        o = x[j:j+1]
        if o == "R":
            columns = columns[int(len(columns)/2):]
        else:
            columns = columns[:int(len(columns)/2)]
    final = (8 * array[0]) + columns[0]
    #if final > highest:
        #highest = final
    #if final < lowest:
        #lowest = final
    seats[final] = 1
     
for i in range(len(seats)):
    if seats[i] == 0:
        print(i)
    
#print(array)
#print(columns)
print(highest)
print(lowest)
print(seats)