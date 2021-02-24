##Написати функцію is_year_leap, приймає 1 аргумент - рік,
##і повертає True, якщо рік високосний,
##і False в іншому випадку

def is_year_leap (year):
    if year % 4 == 0:
        return "True"
    else:
        return "False"

print ("""The program retur: \n'True' - if the yar is high \n'False' - if the year is not high""")
year = int (input ("Input a year: "))
print (is_year_leap (year))
