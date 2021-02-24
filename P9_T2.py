##Створіть словник, ключами якого є країни, а значеннями – список великих
##міст цієї країни. На запит міста, що введений користувачем, програма повинна
##вивести країну, в якій воно знаходиться.

country = {"Belgium": ["Brussels", "Antwerp"],
           "Bulgaria" : ["Sofia", "Varna", "Plovdiv"],
           "Greece" : ["Athens", "Thessaloniki"],
           "Denmark" : ["Copenhagen", "Aarhus"],
           }

sity = input ("Input the sity: ")

for key in country:
    for item in country [key]:
        if item == sity:
            print (key)
       
            
