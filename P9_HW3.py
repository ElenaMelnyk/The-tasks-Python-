##3. У змінній записаний текст. Словом вважається послідовність непорожніх
##символів, які йдуть підряд, слова розділені одним або більше пробілом.
##Програмно створіть словник, в якому ключами є слова з речення, а значеннями –
##кількість входження в речення.

my_string = input ("Input string: ")
split_my_string = my_string.split ()
my_dict = {}
temp = []

for item in split_my_string:
    my_list = [".", ",", ":", ";", "!", "?", "/"]
    for j in range (len (my_list)):
        if my_list [j] in item:
            item = item.replace (item [-1], "")
    temp.append (item)

for i in range (len (temp)):
    count_item =  temp.count (temp[i])
    my_dict.update ({temp[i] : count_item})
    
   
for key, value in my_dict.items():
    print ("{} - {}".format (key, value))
  
