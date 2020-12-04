import sys
string = ""
lines = []
passports = []
total = 0

filename = sys.argv[1]

for line in open(filename, 'r'):
    string += line
lines = string.split('\n\n')



for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", " ")

#print(lines)

for i in range(len(lines)):
    res = lines[i].split(" ")
    passports.append(res)

#print(passports)

for x in passports:
    print(x)
    


for i in range(len(passports)):
    check = 0
    if len(passports[i]) >= 7:
        for j in range(len(passports[i])):
            if passports[i][j][:3] == "byr":
                year = (int(passports[i][j][4:]))
                if year >= 1920 and year <= 2002:
                    check += 1
            elif passports[i][j][:3] == "iyr":
                iyear = (int(passports[i][j][4:]))
                if iyear >= 2010 and iyear <= 2020:
                    check += 1
            elif passports[i][j][:3] == "eyr":
                eyear = (int(passports[i][j][4:]))
                if eyear >= 2020 and eyear <= 2030:
                    check += 1
            elif passports[i][j][:3] == "hgt":
                height = (passports[i][j][4:])
                if height[-2:] == "in":
                    inches = (int(height[:2]))
                    if inches >= 59 and inches <= 76:
                        check += 1
                elif height[-2:] == "cm":
                    try:
                        centi = (int(height[:3]))
                        if centi >= 150 and centi <= 193:
                            check += 1
                    except ValueError:
                        break
            elif passports[i][j][:3] == "hcl":
                hclcheck = 0
                hcl = (passports[i][j][4:])
                #if len(hcl) != 7:
                    #continue
                if hcl[0:1] == "#":
                    hclcheck += 1
                for x in range(1, len(hcl)):
                    val = ord(hcl[x:x+1])
                    #print(val)
                    if (val >= 48 and val <= 57) or (val >= 97 and val <= 102):
                        hclcheck += 1
                #print(hclcheck)
                if hclcheck == 7:
                    check += 1
            elif passports[i][j][:3] == "ecl":
                eye = (passports[i][j][4:])
                if (eye == "amb") or (eye == "blu") or (eye == "brn") or (eye == "gry") or (eye == "grn") or (eye == "hzl") or (eye == "oth"):
                    check += 1
            elif passports[i][j][:3] == "pid":
                pid = (passports[i][j][4:])
                try:
                    if pid[0:2] == '00':
                        f = (int(pid))
                        if f > 999999 and f <= 9999999:
                            check += 1
                    elif pid[0:1] == '0' and pid [1:2] != '0':
                        x = (int(pid))
                        if x > 9999999 and x <= 99999999:
                            check += 1
                    else: 
                        pidr = (int(pid))
                    #print(pid)
                        if pidr > 99999999 and pidr <= 999999999:
                            check += 1
                       
                except ValueError:
                    break
                
        if check == 7:
            total += 1
            


        
    #elif len(passports[i]) == 7:
        #for j in range(len(passports[i])):
            #if passports[i][j][:3] != "cid":
                #check+=1
        #if check == 7:
            #total += 1
    #check = 0

print(total)