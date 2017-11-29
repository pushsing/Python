def sum(o):
    s=0
    for i in o:
        s=s+i
    return s
def multiply(o):
    s=1
    for i in o:
        s=s*i
    return s
l=[1,3,4]
tt=sum(l)
print("Sum:",tt)
rr= multiply(l)
print("Multiply:", rr )