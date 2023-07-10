'''
input: array A[1:n]
output: pairs (i,j)

```
pseudocode:
Get_Inversions(A,n)
    pairs=[]
    for i=1 to n-1
        for j=i to n-1
            if i < j and A[i] > A[j]
                pairs.append((i,j))
    return pairs
    
time complexity: Θ(n^2)
```
'''
import random
def get_inversion(my_list):
    n=len(my_list)-1
    pairs=[]
    for i in range(n-1):
        for j in range(i+1,n):
            if i < j and my_list[i] > my_list[j]:
                pairs.append((i,j))
    return pairs

def generate_list(n):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(0, 1000))
    return my_list

def main():
    n=int(input("Enter number of the list: "))
    my_list = generate_list(n)
    result=get_inversion(my_list)
    print(my_list)
    print(result)
    
main()