def dtob(n):
    if n==0:
        return 0
    else:
        return (n%2+(10*dtob(int(n/2))))

n=int(input("Enter any decimal: "))
print (dtob(n))