# https://www.hackerrank.com/challenges/construct-the-array/problem

def construct_the_array(n,k,x):
    #a represents the array with the number of posibilities which end with x
    #b represents the array with the number of posibilities 
    #which does NOT end with x
    a = [0]*n
    b = [0]*n
    if x == 1:
        a[0] = 1
        b[0] = 0
    else:
        a[0] = 0
        b[0] = 1

    for i in range(1,n):
        a[i] = b[i-1]
        b[i] = (b[i-1] * (k-2)) + (a[i-1] * (k-1))
    return a[n-1]



if __name__ == "__main__":
    
    n, k, x = list(map(int,input().rstrip().split()))

    print(construct_the_array(n,k,x))
