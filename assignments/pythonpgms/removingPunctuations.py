punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s=input("Enter string: ")
op=str()
for i in s:
    if i not in punctuations:
        op=op+i
print(op)