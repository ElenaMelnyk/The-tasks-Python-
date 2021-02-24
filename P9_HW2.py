##2. Створіть словник, ключами є слова, а значеннями – список слів-синонімів
##до нього. Програма отримує на вхід кількість слів N. Далі користувач вводить
##слова-ключі та відповідні йому синоніми. 
##Передбачити: 
##1) на запит (слово) користувача вивести список синонімів;
##2) користувач вводить речення, в якому є слова (ключі, що містяться в словнику).
##Замінити їх синонімами та вивести речення на екран.

dictionary = {}
temp = []
count_words = int (input ("Input the count of words: "))
    
i = 0
while i < count_words:
    word = input ("Input a word: ")
    sinonyms_words = input ("Input synonyms of words: ")
    dictionary.update ({word : sinonyms_words.split(",")})
    i += 1

print ()
print ("Input '#' to stop the program.")
my_string = input ("Input the word(s): ")
list_my_string = my_string.split ()
print ()
while my_string != "#":
    if len (list_my_string) > 1:
        new_string = ''
        for key in dictionary.keys():
            for i in range (len (list_my_string)):
                if list_my_string[i] == key:
                    temp = list_my_string[i]
                    list_my_string[i] = "/". join (dictionary [key])
                    new_string = " ".join (list_my_string)
        print ("\nNew string: \n%s" %new_string)
    elif len (list_my_string)== 1 and my_string not in dictionary.keys():
        print ("The word not in dictionary.")
        print ()
    elif len (list_my_string)== 1 and my_string in dictionary.keys():
        sinonym = dictionary.get (my_string)
        print ("The sinonym is: ", sinonym)
   
                   
    my_string = input ("\nInput the word(s): ")
    list_my_string = my_string.split ()


    
