def max_pairwise_product(A):
    i = A.index( max(A)) # the index of the first element 
    first = A[ i ]
    A[ i ] = 0
    j = A.index( max(A))
    second = A[ j ]
    return first * second

if __name__ == '__main__': # making sure the program that we r running is in this file
    A = list( map( int, input().split() ))  # printing the array of input numbers and converting them to an int( cuz the split renders a string)
    print(max_pairwise_product(A))   
    