m=int(input("Enter no. of rows: "))
n=int(input("Enter no. of columns: "))
print("Enter matrice 1 row wise")
mat1=[]
mat2=[]
for i in range(m):
    mat1=mat1+[input().split()]
print("Enter matrice 2 row wise")
for i in range(m):
    mat2=mat2+[input().split()]
print("Matices sum:")
for i in range(m):
    for j in range(n):
        print (int(mat1[i][j])+int(mat2[i][j]),end=' ')
    print()