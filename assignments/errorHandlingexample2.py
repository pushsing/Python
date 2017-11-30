import sys
x= int(sys.argv[1])
y= float(sys.argv[2])

try:
    if isinstance(x, (int)) and isinstance(y, float):
        print("First Value is int and second value is float")
    else:
        raise ValueError()

except ValueError:
    print(" Error value not int or float")
