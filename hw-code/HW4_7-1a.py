def HoarePartition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    
    counter=0
    while True:
        counter += 1
        print( 'Iteration ' + str(counter) + ':' )
        while True:
            j -= 1
            if A[j] <= x:
                break
        while True:
            i += 1
            if A[i] >= x:
                break
        
        print( 'i = ' + str(i) )
        print( 'j = ' + str(j) )
        
        if i < j:
            A[i], A[j] = A[j], A[i]
            print ('A = ' + str(A))
        else:
            print ('A = ' + str(A))
            return j

A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
print 'Originally... \nA =', A

j = HoarePartition(A, 0, len(A)-1)
print 'After Partition operation... \nA =', A
print 'j =', j
