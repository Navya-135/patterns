def triangle(n):
    x=0
    for i in range(0,n):
        for j in range(0, x):
            print(" ",end=" ")
        x+=1
        for k in range(0,n):
            print("* ",end="")
        n=n-1
        print("\r")
triangle(5)

def triangle(n):
    x=0
    for i in range(0,n):
        for k in range(0,n):
            print("* ",end="")
        for j in range(0, x):
            print(" ",end=" ")
        x+=1
        for j in range(0, x):
            print(" ",end=" ")

        n=n-1
        print("\r")
triangle(5)





def triangle(n):
    for i in range(0,n):
        for j in range(0,i):
             print("* ",end="")
        print("\r")
triangle(6)



def triangle(n):
    x=0
    for i in range(0,n):
        for k in range(0,n):
            print(" ",end="")
        for j in range(0, x):
            print("* ",end=" ")
        x+=1

        n=n-1
        print("\r")
triangle(6)



def triangle(n):
    x=0
    for i in range(0,n):
        for j in range(0,x):
            print(" ",end="")
        x=x+1
        for k in range(0,n):
            print("* ",end=" ")


        n=n-1
        print("\r")
triangle(6)



def triangle(n):
    x=n-1
    for i in range(0,n):
        for j in range(0,x):
            print(" ",end="")
        x=x-1
        for k in range(0,n):
            print("* ",end=" ")


        print("\r")
triangle(6)



def triangle(n):
    x=n-1
    for i in range(1,n):
        for j in range(0,x):
            print(" ",end=" ")
        x=x-1
        for k in range(0,i):
            print("*",end=" ")


        print("\r")
triangle(6)


def triangle(n):
    x=0
    for i in range(0,n):
        lst=[0,1,1,2,3]
        for j in range(0, x):
            print(" ",end=" ")
        x+=1
        for k in range(0,n):
            print(lst[k],end=" ")
        n=n-1
        print("\r")
triangle(5)












