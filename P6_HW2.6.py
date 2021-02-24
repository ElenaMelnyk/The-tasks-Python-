##У матриці 10x10 поміняти значення елементів у кожному рядку,
##розташовані відповідно на головній та бічній діагоналях.


from random import randint
column = 10
row = 10
matr = [[0]*column for i in range(10)]

print ("Matrix")
for i in range(row):
    for j in range(column):
        matr[i][j] = randint(0,100)
        print('%4d' %matr[i][j], end = '')
    print()

temp = []
for i in range(column):
    temp = matr [i][i]
    matr[i][i] = matr[i][column -1 -i]
    matr[i][column -1 -i] = temp

print ()
print ("New Matrix")
for i in range(row):
    for j in range(column):
        print('%4d' %matr[i][j], end = '')
    print()

        
