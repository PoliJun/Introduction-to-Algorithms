# 2.1-5 add binary integers

'''
2.1-5
Consider the problem of adding two n-bit binary integers a and b,
stored in two n-element arrays A[0 : n – 1] and B[0 : n – 1], where each
element is either 0 or 1, , and . The
sum c = a + b of the two integers should be stored in binary form in an
(n + 1)-element array C [0 : n], where . Write a procedure
ADD-BINARY-INTEGERS that takes as input arrays A and B, along
with the length n, and returns array C holding the sum.
'''

# Algorithms
'''
input: A, B
output: C[A.length + 1]
Add-BINARY-INTEGERS(A, B)
    carry=0
    for i=A.length to 1
        C[i+1] = (A[i] + B[i] + carry)%2
        carry=(A[i] + B[i]+carry)/2
    C[1]=carry
'''




import random
def add_binary_integers(a_list, b_list):
    carry = 0
    i = len(a_list)-1
    c_list = list(range(len(a_list)+1))

    # for i in range(len(a_list)):
    while i > 0:
        c_list[i+1] = (a_list[i] + b_list[i]+carry) % 2
        carry = (a_list[i] + b_list[i]+carry)//2
        i -= 1
    c_list[0] = carry
    print(c_list)
    return c_list


def generate_list(n):
    binary_numbers = []
    for i in range(n):
        binary_numbers.append(random.randint(0, 1))
    return binary_numbers


def main():
    size_of_ab_list = int(input("input size of ab list: "))
    a_list = generate_list(size_of_ab_list)
    b_list = generate_list(size_of_ab_list)
    c_list = add_binary_integers(a_list, b_list)
    print("a_list:    ", a_list)
    print("b_list:    ", b_list)
    # add_binary_integers(a_list, b_list)
    print("c_list: ", c_list)
    print(3 % 2)


if __name__ == "__main__":
    main()
