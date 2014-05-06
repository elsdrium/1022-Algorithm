def DiffMatcher(T, P):
    n = len(T)
    m = len(P)
    i = 1
    c = 0
    while i+c < n:
        print i, c
        if T[i+c] != P[c]:
            i = i + max(c, 1)
            c = 0
        else:
            c += 1

        if c == m:
            print( 'Pattern occurs with shift ' + str(i) )
            i += m
            c = 0

DiffMatcher('banuanuan', 'uan')
