A = [[2, 3, 5, 6], [4, 8, 9, 10], [12, 14, 16, 17]]
def Print(matrix):
    for a in matrix:
        print a
    print '\n'

def reYoungnify(A, m_start, m_end, n_start, n_end):
    if m_start != m_end and A[m_start+1][n_start] < A[m_start][n_start]:
        if n_start != n_end:
            if A[m_start][n_start+1] < A[m_start+1][n_start]:
                A[m_start][n_start+1], A[m_start][n_start] = A[m_start][n_start], A[m_start][n_start+1]
                Print(A)
                reYoungnify( A, m_start, m_end, n_start+1, n_end );
        else:
            A[m_start+1][n_start], A[m_start][n_start] = A[m_start][n_start], A[m_start+1][n_start]
            Print(A)
            reYoungnify( A, m_start+1, m_end, n_start, n_end );
            
    elif n_start != n_end and A[m_start][n_start+1] < A[m_start][n_start]:
        A[m_start][n_start+1], A[m_start][n_start] = A[m_start][n_start], A[m_start][n_start+1]
        Print(A)
        reYoungnify( A, m_start, m_end, n_start+1, n_end );
    
def ExtractMin(A):
    retVal = A[0][0]
    print( 'min is    ' + str(retVal) )
    A[0][0] = float('inf')
    
    if len(A) > 1: # check m>1
        if A[1][0] < A[0][0]:
            if len(A[0]) > 1: # check n>1
                if A[0][1] < A[1][0]:
                    A[0][1], A[0][0] = A[0][0], A[0][1]
                    Print(A)
                    reYoungnify( A, 0, len(A)-1, 1, len(A[0])-1 )
            else:
                A[1][0], A[0][0] = A[0][0], A[1][0]
                Print(A)
                reYoungnify( A, 1, len(A)-1, 0, len(A[0])-1 )
    else:
        if len(A[0]) > 1: # check n>1
            if A[0][1] < A[1][0]:
                A[0][1], A[0][0] = A[0][0], A[0][1]
                Print(A)
                reYoungnify( A, 0, len(A)-1, 1, len(A[0])-1 )

ExtractMin(A)
