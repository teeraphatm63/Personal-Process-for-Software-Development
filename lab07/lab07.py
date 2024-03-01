""" Calculat parameters for a simple linear regression between time and size

    Author: Teeraphat Muaksang 
    Since: 2023 july 27
    Compiler: Python 3.11.4
    Platform: Window 11 Pro 64-bit

"""

def avgOfX():
    file = open('lab07/data_x.txt')
    list_of_x = file.read().split()
    size_of_x = int(len(list_of_x))
    sum_of_x = 0
    avg_of_x = 0
    for data in list_of_x:
        all_data = float(data)
        sum_of_x = sum_of_x + all_data
        avg_of_x = sum_of_x/size_of_x
    return avg_of_x
avg_x = avgOfX()

def avgOfY():
    file = open('lab07/data_y.txt')
    list_of_y = file.read().split()
    size_of_y = int(len(list_of_y))
    sum_of_y = 0
    avg_of_y = 0
    for data in list_of_y:
        all_data = float(data)
        sum_of_y = sum_of_y + all_data
        avg_of_y = sum_of_y/size_of_y
    return avg_of_y
avg_y = avgOfY()


def crossOfXdelY():
    file = open('lab07/data_x.txt')
    file1 = open('lab07/data_y.txt')
    list_of_data = file.read().split()
    list_of_data1 = file1.read().split()
    list_of_x = []
    list_of_y = []
    sum_of_x = 0
    sum_of_y = 0
    for data in list_of_data:
        all_data = float(data)
        sum_of_x = all_data - avg_x
        list_of_x.append(sum_of_x)
    for data1 in list_of_data1:
        all_data1 = float(data1)
        sum_of_y = all_data1 - avg_y
        list_of_y.append(sum_of_y)
    return list_of_x,list_of_y
lis_x,list_y = crossOfXdelY()

def sumOfXCrssY():
    total_of_sum = 0
    for i in range(len(lis_x)):
        x_crss_y = (lis_x[i]*list_y[i])
        total_of_sum = total_of_sum + x_crss_y
    return total_of_sum
sum_of_x_crss_y = sumOfXCrssY()

def findXidelXbarSquare():
    file = open('lab07/data_x.txt')
    list_of_x = file.read().split()
    sum_of_dex_x_sq = 0
    num_in_list = 0
    for data in list_of_x:
        all_data = float(data)
        num_in_list = (all_data - avg_x)**2
        sum_of_dex_x_sq = sum_of_dex_x_sq + num_in_list
    return sum_of_dex_x_sq
sum_of_delta_x_square = findXidelXbarSquare()

beta1 = sum_of_x_crss_y/sum_of_delta_x_square
beta0 = avg_y - (beta1*avg_x)
print('Linear Regression value = ',beta0)
