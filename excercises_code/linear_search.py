# 2.1-4 write a liner search
# input: sorted list, x
# output: index of value x in list

# Algorithms
'''
Find_Value(A, x)
    for i=1 to len(A)
        if A[i] == x
            return i
    return -1      
'''
my_list = input('input a list:\n').split()


def find_value(sorted_list, x):
    for i in range(len(sorted_list)):
        if int(sorted_list[i]) == x:
            print(i)
            return i
    print(-1)
    return -1


find_value(my_list, 12)
