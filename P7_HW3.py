##Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
##і повертає 3 значення (за допомогою кортежу): периметр квадрата,
##площу квадрата і діагональ квадрата.

def square (side):

    from math import sqrt

    perimeter_square = side * 4
    area_square = side ** 2
    diagonal_square = sqrt (side ** 2 + side ** 2)

    return ("The perimeter of the square is: %d \nThe area of the square is: %d \nThe diagonal of the square is: %.2f" %(perimeter_square, area_square, diagonal_square))
    
print ("The program calculate the perimetr, area, diagonal of square")
side = int (input ("Input the size of the square's side: "))
print (square (side))
