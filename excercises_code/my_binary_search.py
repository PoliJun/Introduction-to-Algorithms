import random


def binary_search(A, k):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < k:
            left = mid + 1
        elif A[mid] > k:
            right = mid - 1
        else:
            return mid
    return -1


def generate_list(n):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(0, 1000))
    return my_list


def main():

    n = 200
    my_list = generate_list(n)
    result = binary_search(my_list, k=68)

    print(my_list, result)
    if result != -1:
        return
    return main()


main()
