import math

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = [None]*(n1+1)
    R = [None]*(n2+1)
    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    
    L[n1] = float('inf')
    R[n2] = float('inf')
    i=0
    j=0
    count=0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += (n1-i)
            
    return count

def CountInversions(A, p, r):
    if p < r:
        q = int(math.floor((p+r)/2))
        return CountInversions(A, p, q) + CountInversions(A, q+1, r) + merge(A, p, q, r)
    else:
        return 0

A = [5, 2, 4, 3, 8, 7]
print CountInversions(A, 0, len(A)-1)
