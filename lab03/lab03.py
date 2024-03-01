""" Determine the second smallest numbers given data are unique.

    Author: Teeraphat Muaksang
    Since: 2023 july 4
    Compiler: Python 3.11.4
    Platform: Window 11 Pro 64 bit

"""

def find2sdSmallest():
    """ Determine the 2nd smallest number from the list

    Return
        the 2nd smallest number.
    """
    file = open('Personal Process for Software Development/lab03/data.txt')
    list_of_num = file.read().split()
    print('list of number = ',list_of_num)
    size_of_num = len(list_of_num)
    for i in range(size_of_num):
        for j in range(0,size_of_num-i-1):
            if int(list_of_num[j])>int(list_of_num[j+1]):
                sort_num = list_of_num[j]
                list_of_num[j] = list_of_num[j+1]
                list_of_num[j+1] = sort_num
    print('the 2nd smallest number = ',list_of_num[1])
find2sdSmallest()