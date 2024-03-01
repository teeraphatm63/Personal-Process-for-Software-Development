""" Caculate basic statistics value from data 

    Author: Teeraphat Muaksang
    Since: 2023 july 5 
    Compiler: Python 3.11.4
    Platform: Window 11 Pro 64-bit
"""
def calBasicStat():

    file = open('lab04/data.txt')
    list_of_num = file.read().split()
    size_of_num = int(len(list_of_num))
    sum_of_num = 0
    avg_of_num = 0
    num_in_list = 0
    sum_of_num_in_list = 0
    print('List of number = ',list_of_num)
    #min to max and show min/max value
    for i in range(size_of_num):
        for j in range(0,size_of_num-i-1):
            if int(list_of_num[j]) > int(list_of_num[j+1]):
                sort_of_num = list_of_num[j]
                list_of_num[j] = list_of_num[j+1]
                list_of_num[j+1] = sort_of_num
    print('Min number = ',list_of_num[0])
    print('Max number = ',list_of_num[-1])
   #calculate median value
    if size_of_num %2 == 1:
        med_value = size_of_num//2
        print('Median value = ',list_of_num[med_value])
    else:
        x = size_of_num//2 -1
        y = size_of_num//2
        med_value = (int(list_of_num[x]) + int(list_of_num[y]))/2
        print('Median value = ',med_value)
    #calculate average value
    for data in list_of_num:
        all_number = int(data)
        sum_of_num = sum_of_num + all_number
        avg_of_num = sum_of_num/size_of_num
    print('Average value = ',avg_of_num)
    #calculate S.D. value
    for data in list_of_num:
        all_number = int(data)
        num_in_list = (all_number - avg_of_num)**2
        sum_of_num_in_list = sum_of_num_in_list + num_in_list
        sd_of_num = (sum_of_num_in_list/size_of_num)**0.50
    print('S.D. = ',sd_of_num)
    print('Number of data =',size_of_num)

calBasicStat()
