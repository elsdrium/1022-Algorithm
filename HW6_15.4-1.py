X = '10010101'
Y = '010110110'

m = len(X)
n = len(Y)
b = [ [0 for _ in range(0,n+1)] for _ in range(0,m+1) ]
c = [ [0 for _ in range(0,n+1)] for _ in range(0,m+1) ]
for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            c[i][j] = c[i-1][j-1] + 1
            b[i][j] = '\\'
        else:
            if c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '-'

import sys
def printLCS(i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '\\':
        printLCS(i-1, j-1)
        sys.stdout.write( X[i-1] )
    elif b[i][j] == '|':
        printLCS(i-1, j)
    else:
        printLCS(i, j-1)

printLCS(m, n)
