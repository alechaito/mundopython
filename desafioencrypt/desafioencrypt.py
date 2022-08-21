from math import sqrt

string = "haveaniceday"
size = sqrt(len(string))

rows = int(size)
columns = int(size) + 1

print(rows, columns)

splited = [string[letter:columns+letter] for letter in range(0, len(string), columns)]


print(splited)
final = ""
for i in range(0, columns):
    for j in range(0, rows):
        final += splited[j][i]
    final += " "

print(final)


#for x in range(0, rows):
#print(splited[0][0], splited[1][0], splited[2][x])


