y=input()
o= "Rovarspraket translation is : "
list=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in y:
    x= i.lower()
    if x in list:
        o=o+i+'o'+i
    else:
        o=o+i
print(o)