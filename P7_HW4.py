##Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
##і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).

def season (number_of_month):
    winter = "12", "1", "2"
    spring = "3", "4", "5"
    summer = "6", "7", "8"
    autumn = "9", "10", "11"

    if number_of_month in winter: return ("Winter.")
    if number_of_month in spring: return ("Spring.")
    if number_of_month in summer: return ("Summer.")
    if number_of_month in autumn: return ("Autumn.")


print ("do you want to know what the season is now?")
number_of_month = input ("Input the number  of the month: ")
print ("The season is: ", season (number_of_month))



