X = '10010101'
Y = '010110110'

m = len(X)
n = len(Y)
c = [ [float('-inf') for _ in range(0,n+1)] for _ in range(0,m+1) ]

def LCSLength(i, j):
    if i == 0 or j == 0:
        return 0

    if c[i-1][j] == float('-inf'):
        c[i-1][j] = LCSLength(i-1, j)

    if c[i][j-1] == float('-inf'):
        c[i][j-1] = LCSLength(i, j-1)

    if c[i-1][j-1] == float('-inf'):
        c[i-1][j-1] = LCSLength(i-1, j-1)

    if X[i-1] == Y[j-1]:
        return c[i-1][j-1] + 1
    else:
        return max( c[i-1][j], c[i][j-1])


print LCSLength(m, n)
