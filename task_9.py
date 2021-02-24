## 9. International Greetings
## Suppose you have a guest list of students and the country they are from, stored
## as key-value pairs in a dictionary.
## GUEST_LIST = {
## "Randy": "Germany",
## "Karla": "France",
## "Wendy": "Japan",
## "Norman": "England",
## "Sam": "Argentina"
## }
## Write a function that takes in a name and returns a name tag, that should read:
## "Hi! I'm [name], and I'm from [country]."
## If the name is not in the dictionary, return:
## "Hi! I'm a guest."

def identify_student (name):
    if name in GUEST_LIST:
        return print ("Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name]))
    else:
        return print ("Hi! I'm a guest.")

GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
    }
name = input ("Input the name of the student: ")
identify_student (name)
