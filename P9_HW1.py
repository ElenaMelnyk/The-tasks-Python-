##1. Створіть словник, зв'язавши його з змінною school, і наповніть його даними,
##які б відображали кількість учнів в десяти різних класах
##(наприклад, 1а, 1б, 2б, 6а, 7в тощо.).
##Дізнайтеся скільки людей в певному класі.
##Уявіть, що в школі відбулися зміни, додайте їх в словник:
##- В трьох класах змінилося кількість учнів;
##- В школі з'явилося два нових класи;
##- В школі розформували один з класів.
##Виведіть вміст словника на екран.

pupils = {school : school + 10 for school in range (1,11)}
print ("Old list")
for key, value in pupils.items():
    print ("class {} - {} pupils".format (key, value))

pupils[2] = 22
pupils[5] = 18
pupils[10] = 32
pupils.update ({"a1" : 4, "b5" : 10})
pupils.pop (6)
print ()
print ("New list")
for key, value in pupils.items():
    print ("class {} - {} pupils".format (key, value))
