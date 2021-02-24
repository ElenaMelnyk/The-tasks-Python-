##Задано символьний рядок,. Розробити програму, яка знаходить групи цифр,
##записаних підряд, і вилучає із них всі початкові нулі, крім останнього,
##якщо за ним знаходиться крапка. Друкує модифікований масив по сорок символів
##у рядку.

strOfSymbols = input('Input string ')
numbers = set()

for i in range(10):
    numbers.add(str(i))
numbers.add('.')

listOfNumbers = []
i = 0
while i < len(strOfSymbols):
    if strOfSymbols[i] in numbers:
        temp = ''
        while strOfSymbols[i]  in numbers and i < len(strOfSymbols):
            temp += strOfSymbols[i]
            i += 1
        listOfNumbers.append(temp)
    i += 1

print(listOfNumbers)

listOfFloat = []
for item in listOfNumbers:
    if '.' in item and len(item) > 1:
        temp = ''
        pos = item.index('.')
        for i in range(pos):
            if item[i] != '0':
                temp += item[i]
        temp += item[pos:]
        
        if temp[0] == '.':
            temp = '0' + temp
        listOfFloat.append(temp)

print(listOfFloat)
