## 10. Stupid Addition
## Create a function that takes two parameters and, if both parameters are strings,
## add them as if they were integers or if the two parameters are integers,
## concatenate them.

def params (param1, param2):
    if type(param1) == int and type(param2) == int:
        str_param = str(param1) + str(param2)
        return print (str_param)
    elif type(param1) == str and type(param2) == str:
        sum_param = int(param1) + int (param2)
        return print (sum_param)
    else:
        return print ("None")


param1 = "5"
print ("param1 = ", param1)
param2 = "11"
print ("param2 = ", param2)
params (param1, param2)

param1 = 34
print ("param1 = ", param1)
param2 = 45
print ("param2 = ", param2)
params (param1, param2)

param1 = 34
print ("param1 = ", param1)
param2 = [45]
print ("param2 = ", param2)
params (param1, param2)
