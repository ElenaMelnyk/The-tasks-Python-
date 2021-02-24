##Вивести на екран «прямокутник», утворений з двох видів символів.
##Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

print ("This program paints a rectangle by the symbols.")
x = input ("Input a symbol: ")
y = input ("Input a symbol: ")
z = " "
a = int (input ("Input first side of rectangle: "))
b = int (input ("Input second side of rectangle: "))

print (z * 4 + y * (b + 2))
for i in range (a):
    print (z * 4 + y + x * b + y)
print (z * 4 + y * (b + 2))


