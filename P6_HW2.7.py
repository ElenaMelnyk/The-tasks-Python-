from random import randint

matr = [[0]*5 for i in range(5)]
matr_new = [[0]*5 for i in range(5)]


for i in range(5):
    for j in range(5):
        matr[i][j] = randint(0,100)
        print('%4d' %matr[i][j], end = '')
    print()

temp_list = []
for j in range(5):
    temp_list.append(matr[0][j])

sorted_temp_list = sorted(temp_list)

print(sorted_temp_list)

index_list = []
for item in sorted_temp_list:
    index_list.append(temp_list.index(item))

print(index_list)
        
for j in range(5):
    for i in range(5):
        matr_new[i][j] = matr[i][index_list[j]]
        
for i in range(5):
    for j in range(5):
        print('%4d' %matr_new[i][j], end = '')
    print()

        
