n=int(input("Enter the number of terms: "))
s=0
t=1
c=0
if n<=0:
    print("Enter valid input")
elif n==1:
    print("Fibonacci Sequence upto", n, "terms : ",0)
else:
    print("Fibonacci Sequence upto", n, "terms : ")
    while c<n:
        print(s,end=',')
        x=s+t
        s=t
        t=x
        c=c+14