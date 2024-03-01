""" Calculate Corelation Value.

    Author: Teeraphat Muaksang
    Since: 2023 july 15
    Compiler: Python 3.11.4
    Platform: Window 11 Pro 64-bit

"""
def avgofActSize ():
    file = open('lab06/size.txt')
    list_of_data = file.read().split()
    size_of_data = int(len(list_of_data))
    sum_of_data = 0
    avg_of_actual_size = 0
    for data in list_of_data:
        all_data = int(data)
        sum_of_data = sum_of_data + all_data
        avg_of_actual_size = sum_of_data/size_of_data
    return avg_of_actual_size
avg_value_of_size = avgofActSize()

def avgOfActTime():
    file = open('lab06/time.txt')
    list_of_data = file.read().split()
    size_of_data = int(len(list_of_data))
    sum_of_data = 0
    avg_of_actual_time = 0
    for data in list_of_data:
        all_data = int(data)
        sum_of_data = sum_of_data + all_data
        avg_of_actual_time = sum_of_data/size_of_data
    return avg_of_actual_time
avg_value_of_time = avgOfActTime()

def xDelXbar():
    file = open('lab06/size.txt')
    list_of_data = file.read().split()
    sum_of_del_x = 0
    num_in_list = 0
    for data in list_of_data:
        all_data = int(data)
        num_in_list = (all_data - avg_value_of_size)**2
        sum_of_del_x = sum_of_del_x + num_in_list
        sqr_of_x  = (sum_of_del_x)**0.5
    return sqr_of_x
sum_of_delta_x = xDelXbar()

def yDelYbar():
    file = open('lab06/time.txt')
    list_of_data = file.read().split()
    sum_of_del_y = 0
    num_in_list = 0
    for data in list_of_data:
        all_data = int(data)
        num_in_list = (all_data - avg_value_of_time)**2
        sum_of_del_y = sum_of_del_y + num_in_list
        sqr_of_y  = (sum_of_del_y)**0.5
    return sqr_of_y
sum_of_delta_y = yDelYbar()

def crossOfXdelY():
    file = open('lab06/size.txt')
    file1 = open('lab06/time.txt')
    list_of_data = file.read().split()
    list_of_data1 = file1.read().split()
    list_of_x = []
    list_of_y = []
    sum_of_x = 0
    sum_of_y = 0
    for data in list_of_data:
        all_data = int(data)
        sum_of_x = all_data - avg_value_of_size
        list_of_x.append(sum_of_x)
    for data1 in list_of_data1:
        all_data1 = int(data1)
        sum_of_y = all_data1 - avg_value_of_time
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
        
R = sum_of_x_crss_y/(sum_of_delta_x * sum_of_delta_y)
print("Correlation Value = ",R)



    



