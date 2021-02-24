## Imagine a circle and two squares: a smaller and a bigger one. For the smaller
## one, the circle is a circumcircle and for the bigger one, an incircle.
## 
## Create a function, that takes an integer (radius of the circle) and returns
## the square area of the square inside the circle.

def square_area(radius):
    return radius**2 + radius**2

radius = int (input("Input the radius of the circle "))
print ("The area of the square inside the circle is %.2f" %square_area(radius))
