#Creating A List and Accessing by Index:
LIST1=["hi","this","is","list"]
LIST2=[9,2,3]
LIST3=["string",42,True,False,8.9]
print(LIST1)
print(LIST2[1])
print(LIST3[2])

#Index Reassignment and .append():
var=[1,2,3]
var[0]=2
var[1]=3
var[2]=4
var.append(6)
print(var)

#List Slicing:
var2=["a",23,67.0,'as',234,456,'the']
print(var2[:5])
print(var2[2:6])
print(var2[1:])

#.index() and .insert()
var3=["Bob Dylan", "Like a", "Rolling Stone"]
print('Index for Rolling Stone is : '+ str(var3.index("Rolling Stone" )))
var3.insert(0, '1965')
print(var3)

#.remove() and .pop()
var4= ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
var4.remove("Sutcliffe")
print(var4)
print(var4.pop(1))
print(var4.pop(2))
print(var4)
