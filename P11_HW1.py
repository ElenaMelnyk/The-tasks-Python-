##1. В класі Person визначте метод compare_age(), який повертатиме результат
##порівняння віку людини з Вашим віком. При заданих об’єктах p1, p2 і p3, які
##будуть ініціалізовані name та age, буде повертатися повідомлення наступного
##формату:
##{other_person} is {older than / younger than / the same age as} me.

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def compare_age (self):
        difference = self.age - 35
        if difference > 0:
            print (self.name, "is older than me." )
        if difference < 0:
            print (self.name, "is younger than me." )
        if difference == 0:
            print (self.name, "is the same age as me." )

p1 = Person ("Tanya", 45)
p2 = Person ("Rita", 28)
p3 = Person ("Inna", 35)
p1.compare_age()
p2.compare_age()
p3.compare_age()
