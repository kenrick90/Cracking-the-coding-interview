def construct_the_array(n,k,x):
    #a represents the array with the number of posibilities which end with x
    #b represents the array with the number of posibilities 
    #which does NOT end with x
    b = [0]*n
    if x == 1:
        b[0] = 0
        b[1] = k-1
    else:
        b[0] = 1
        b[1] = k-2

    for i in range(2,n):
        #a[i] = b[i-1]
        b[i] = ((b[i-1] * (k-2)) + (b[i-2] * (k-1))) % 1000000007
    return b[n-2]



if __name__ == "__main__":
    
    n, k, x = list(map(int,input().rstrip().split()))

    print(construct_the_array(n,k,x))
