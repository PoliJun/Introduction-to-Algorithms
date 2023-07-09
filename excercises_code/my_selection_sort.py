'''
input: array A[1:n]
output: sorted array A
Algorithms:

1. Through A, find the minimum
2. swap with A[1]
3. Through A[2:n], finde the minimum
4. swap with A[2]
...
5. Until through all A and sort.

Pseudocode:

Selection_Sort(A)
    min=0
    for i=1 to A.length
        for j=i to A.length
            if A[j] < min
                min = A[j]
        A[i] = min
    return A
        
'''

import random


def my_sort(my_list):
    for i in range(len(my_list)):
        my_min = my_list[i]
        for j in range(i, len(my_list)):
            if my_list[j] < my_min:
                my_min = my_list[j]
                my_list[j] = my_list[i]
                my_list[i] = my_min
    return my_list


def generate_list(n):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(0, 100))
    return my_list


def main():
    n = int(input("Enter the number of your list: "))
    my_list = generate_list(n)
    print("unsorted list: {}".format(my_list))
    my_list = my_sort(my_list)
    print("sorted list: {}".format(my_list))


main()
