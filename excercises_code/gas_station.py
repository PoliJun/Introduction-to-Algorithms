# @param A,B list of integers
# @return an integer

def can_complete_circuit(A, B):
    n = len(A)

    curr = start = 0

    for i, (g, c) in enumerate(zip(A*2, B*2)):
        if i == start+n:
            return start

        curr += g-c

        if curr < 0:
            start = i+1  # we don't have to test start+1 because evev the original gas>0, still curr<0
            curr = 0

    return -1
