"""
* Author: Chen Hsueh-Min
* Date  : 2014/05/04
* Info  : This is an implementation of merge sort algorithm in Python. Be aware to that Python list starts from index 0.
"""

def ComputePrefix(P):
    m = len(P)
    pi = [ -1 for _ in range(0,m) ]
    k = -1
    for q in range(1, m):
        while k = 0 and P[k+1] != P[q]:
            k = pi[k]
        if P[k+1] == P[q]:
            k = k + 1
        pi[q] = k
    return pi

def KMPMatcher(T, P):
    n = len(T)
    m = len(P)
    pi = ComputePrefix(P)
    q = -1

    for i in range(0, n):
        while q = 0 and P[q+1] != T[i]:
            q = pi[q]
        if P[q+1] == T[i]:
            q = q + 1
        if (q+1) == m:
            print( 'Pattern occurs with shift ' + str(i+1-m) )
            q = pi[q]

T = 'banana'
P = 'ana'
KMPMatcher(T, P)
