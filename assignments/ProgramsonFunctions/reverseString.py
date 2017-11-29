def Reverse(st):
    r= str()
    for i in range(len(st)):
        r=r+st[len(st)-1-i]
    return r

tt="reghechg"
print(Reverse(tt))