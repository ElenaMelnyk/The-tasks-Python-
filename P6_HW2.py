##Заповнити список дійсними числами введенням з клавіатури.
##Порахувати суму і добуток елементів списку.
##Вивести на екран сам список, отримані суму і добуток його елементів.

str_list1 = input ("Input a number (use a space for separate them): ")
list1 = str_list1.split ()
for number in range (0, len (list1)):
    list1[number] = float (list1[number]) 
print ("List: ", list1)

sum_list1 = sum (list1)
print ("The sum of all elements in list is: ", sum_list1)

multiply_list1 = 1
for item in range (len (list1)):
    multiply_list1 *= list1 [item]
print ("The multiply of all elements in list is: ", multiply_list1)
