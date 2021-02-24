## 12. Concatenate Variable Number of Input Lists
## Create a function that concatenates n input lists, where n is variable.
## Examples
## concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
##
## concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
##
## concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]




def full_list (n):
    full_list = []
    for item in n:
        for i in range (len(item)):
            full_list.append (item[i])
    sort_full_list = sorted(full_list)
    return print (sort_full_list)
   
        


print ("For stop the program input #")
n = [1], [4,5], [6, 7, 9, 0], [11, 6, 88], [-1], [100]
full_list (n)
