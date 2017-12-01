m=int(input("Enter no. of rows: "))
n=int(input("Enter no. of columns: "))
if m!=n:
    print("invalid input")
    exit()
print("Enter matrice row wise")
mat=[]
for i in range(m):
    mat=mat+[input().split()]
print("Transpose: ")
for i in range(m):
    for j in range(n):
        print (int(mat[j][i]),end=' ')
    print()