p = [5, 10, 3, 12, 5 ,50, 6]
#p = [30, 35, 15, 5, 10, 20, 25]

n = len(p)-1
m = [ [0 for _ in range(0,n)] for _ in range(0,n) ]
s = [ [0 for _ in range(0,n)] for _ in range(0,n) ]

for l in range(2, n+1): # l from 2 to n
    for i in range(0,n-l+1):
        j = i + l - 1
        if i == j:
            m[i][j] = 0
        else:
            m[i][j] = float("inf")
        for k in range(i, j):
            q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k

import sys
def pop(s, i, j):
    if i == j:
        sys.stdout.write('A' + str(i))
    else:
        sys.stdout.write( '(' )
        pop(s, i, s[i][j])
        pop(s, s[i][j]+1, j)
        sys.stdout.write( ')' )

pop(s,0,n-1)
