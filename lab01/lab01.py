""" Find the summation of number 1 to 100.

    Authotr: Teeraphat Muaksang
    Since: 2023 july 5
    Compiler: Python 3.11.4
    Platform: Window 11 Pro 64-bit

"""
def sum1to100():
    summation = 0
    for i in range(1,101):
        summation = summation + i
    print('Summation of number 1 to 100 = ',summation)
sum1to100()