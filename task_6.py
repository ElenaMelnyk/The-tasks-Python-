##6. Date Format
##Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

def date_formatted (date):
    new_date= date.replace ("/", "")
    i = len(new_date)-1
    rev_date = ""
    while i >= 0: 
        rev_date += new_date [i]
        i -= 1
    return rev_date

date = input ("Input the date ")
print (date_formatted (date))




