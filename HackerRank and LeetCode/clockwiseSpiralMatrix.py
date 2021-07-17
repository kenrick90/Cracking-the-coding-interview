
def solution(a):
    y = len(a)
    x = len(a[0])

    x1=0
    y1=0
    x2=x-1
    y2=y-1

    output=[]
    while x1 <= x2 or y1 <= y2 :
        for n in range(x1,x2+1):
            output.append(a[y1][n])

        for m in range(y1+1,y2+1):
            output.append(a[m][n])

        if x1 != x2 and y1 != y2:
            for n in range(x2-1,x1-1,-1):
                output.append(a[m][n])

            for m in range(y2-1,y1,-1):
                output.append(a[m][n])
        x2-=1
        y2-=1
        y1+=1
        x1+=1
    print(output)

if __name__ == "__main__":

    x = int(input("Enter the number of columns"))
    y = int(input("Enter the number of rows"))

    a = [[int(input("Enter a single digit")) for _ in range(x)] for _ in range(y)]

    solution(a)
    print(a)
