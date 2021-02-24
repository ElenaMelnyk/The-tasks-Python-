
def sum_numbers (str_numbers):
    list_numbers = list (str_numbers.split ())
    int_numbers = []
    for i in range (len (list_numbers)):
        int_numbers.append (int (list_numbers [i]))   
    return sum (int_numbers)



def main ():
    print ("The program count the sum of numbers.")
    print ("Input # to stop the program.")
    sum_total = 0
    while True: 
        str_numbers = input ("Input numbers: ")
        if '#' in str_numbers:
            sum_total += sum_numbers (str_numbers[:str_numbers.find ('#')])
            print ("The sum of numbers is: ", sum_total)
            break
        sum_total += sum_numbers (str_numbers)
        print ("The sum of numbers is: ", sum_total)

if __name__ == "__main__":
    main()
