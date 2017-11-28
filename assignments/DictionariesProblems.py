#Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:
var1={'Name': 'Zack', 'Age': 78, 'Class': 'xii'}
print(var1['Age'])
var1['School'] = "VKS";
print(var1)
print('Length of var1: '+str(len(var1)))

#Reassignment by Key and Del:
var2={'city':'MBD','state':'UP'}
print(var2)
var2['city']='CNB'
print(var2)
del var2['city'];
print(var2)