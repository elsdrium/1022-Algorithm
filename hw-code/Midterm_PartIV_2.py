import math

def FindPartition(A):
    n = len(A)
    S = sum(A)
    halfS = int(math.floor(S/2))
    P = [ [None for _ in range(0, (n+1))] for _ in range(0, (halfS+1)) ]
    for i in range(1, halfS+1):
        P[i][0] = False
    for j in range(0, n+1):
        P[0][j] = True

    for i in range(1, halfS+1):
        for j in range(1, n+1):
            if i >= A[j-1]:
                P[i][j] = (P[i][j-1] or P[i-A[j-1]][j-1])
            else:
                P[i][j] = P[i][j-1]
    return P[halfS][n]

A = [2, 2, 2]
FindPartition(A)
