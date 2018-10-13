n = 5
root_table = [[1, 1, 2, 2, 2], [0, 2, 2, 2, 4], [0, 0, 3, 4, 5], [0, 0, 0, 4, 5], [0, 0, 0, 0, 5]]

def ConstructOptimalBST(root):
    r = root[0][n-1]-1
    print( 'k' + str(r) + ' is the root')
    ConstructOptimalSubBST(root, 0, r-1, 'left', r)
    ConstructOptimalSubBST(root, r+1, n-1, 'right', r)

def ConstructOptimalSubBST(root, i, j, direction, parent):
    if i <= j:
        r = root[i][j]-1
        print( 'k' + str(r) + ' is the ' + direction + ' child of k' + str(parent) )
        ConstructOptimalSubBST(root, i, r-1, 'left', r)
        ConstructOptimalSubBST(root, r+1, j, 'right', r)
    else:
        if direction == 'left':
            print( 'd' + str(parent-1) + ' is the left child of k' + str(parent) )
        else:
            print( 'd' + str(parent) + ' is the right child of k' + str(parent) )

ConstructOptimalBST(root_table)
