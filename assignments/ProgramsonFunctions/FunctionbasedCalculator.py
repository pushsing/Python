t=input("Calculate: ")
def calculator(t):
    x=t.split()
    x[0] = int(x[0])
    x[2] = int(x[2])
    if x[1]=='+':
        print(x[0]+x[2])
    elif x[1]=='-':
        print(x[0]-x[2])
    elif x[1] == '*':
        print(x[0] * x[2])
    elif x[1] == '/':
        print(x[0] / x[2])

calculator(t)