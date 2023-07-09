# ````
# for i=2 to n
# key = A[i]
# j = i-1
#   while j>0 and A[j] < key
#       A[j+1]=A[j]
#       j=j-1
# A[j+1]=key
# ````


l = [4, 6, 8, 2, 1, 69, 7]
for i in range(1, len(l)):
    key = l[i]
    j = i-1
    while j >= 0 and l[j] < key:
        l[j+1] = l[j]
        j = j-1
    l[j+1] = key
print(l)
