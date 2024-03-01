""" Find the summation of even number form data.

    Author: Teeraphat Muaksang
    Since: 2023 july 4
    Compiler: Python 3.11.4
    Platform: Window 11 Pro 64-bit

"""
def sumOfEvenNum():

    file = open('Personal Process for Software Development/lab02/data.txt')
    list_of_number = file.read().split()
    sum_even = 0
    for data in list_of_number:
        all_number = int(data)
        if all_number % 2 == 0:
            sum_even = sum_even + all_number
    print('The summation of even number = ',sum_even)
sumOfEvenNum()