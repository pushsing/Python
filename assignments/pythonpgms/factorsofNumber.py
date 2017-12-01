import math
def findfactors(n):
    f=[]
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            if(n/i==i):
                f=f+[i]
            else:
                f=f+[i]+[int(n/i)]
    return f
x=int(input("Enter number: "))
print("factors of ",x,": ",findfactors(x))
