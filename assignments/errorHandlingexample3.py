import sys
f=sys.argv[1]


try:
    file_object=open(f,'r+')
    print("File opened successfully")
except FileNotFoundError:
    print("File doesn't exist")
except IOError:
    print("Can not read file")
