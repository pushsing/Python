print("Enter three numbers:")
x=int(input())
y=int(input())
z=int(input())
if x<y | x<z :
    if y>z:
        print( y, "is maximum")
    else:
        print(z, "is maximum")
elif y>z :
    if y>x:
        print( y, "is maximum")
    else:
        print(x, "is maximum")
else:
    if x>z:
        print( x, "is maximum")
    else:
        print(z, "is maximum")
