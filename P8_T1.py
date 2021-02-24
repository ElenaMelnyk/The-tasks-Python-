##1. Ввести кортеж. Створити список з його елементів, що впорядковані за зростанням.

y = 2, 4, 0, 12, 45, 8
print (y)
y = tuple (sorted (y))
print (y)

##2. Задано список кортежів 
##grades=[(“Ann”, 4), (“Bob”, 2), (“Elizabeth”, 3), (“Dan”, 5)] 
##Вивести на екран послідовність вигляду: 
##“Hello, Ann! Your grade is 4.”

print ()
grades=[("Ann", 4), ("Bob", 2), ("Elizabeth", 3), ("Dan", 5)]
print ("Hello, %s! Your grade is %d." % (grades [0][0], grades[0][1]))


##3.    Задано кортеж 
##names=(“Ann”, “Bob”, “Elizabeth”, “Mr. McMullen”, “Mrs. Smith”). 
##Вивести на екран послідовність привітань, але таким чином, щоб ті,
##хто записаний за іменами, вітати словом «Hello», а «Mr.» чи «Mrs.» вітати Good morning.

print ()
names=("Ann", "Bob", "Elizabeth", "Mr. McMullen", "Mrs. Smith")
for item in names:
       if "." in item:
           print ("Hello %s!" %item)
       else:
           print ("Good morning %s!" %item)
           
        
