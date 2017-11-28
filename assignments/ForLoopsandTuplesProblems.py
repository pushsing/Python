#Tuples:
tup1 = (45.12, 'chennai', True, 2017);
print(tup1)
print(tup1[1])
print(tup1[0])
print(tup1[:3])
print(tup1[1:])
print(tup1[1:3])

#For Loops:
tup2=("Bohr", "Leibniz", "Einstein")
var=[]
var2= [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(tup1)):
    print(tup1[i])
for i in range(6):
    var.append(var2[i+2])
print(var)