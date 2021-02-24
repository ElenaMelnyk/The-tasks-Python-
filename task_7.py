## 7. Check If Lines Are Parallel
## Given two lines, determine whether or not they are parallel.
## Lines are represented by a list [a, b, c], which corresponds to
## the line ax+by=c.


def check_lines (a1, b1, a2, b2):
    if a1 * b2 - a2 * b1 == 0:
        return "True"
    else:
        return "False"

first_line = input ("Input first line ")
str_first_line = first_line.split (",")
list_first_line = [int (str_first_line[i]) for i in range (len (str_first_line))]
second_line = input ("Input second line ")
str_second_line = second_line.split (",")
list_second_line = [int (str_second_line[i]) for i in range (len (str_second_line))]
a1 = list_first_line [0]
b1 = list_first_line [1]
a2 = list_second_line [0]
b2 = list_second_line [1]

print ("Are the lines parallel? " , check_lines (a1, b1, a2, b2))




