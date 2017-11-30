import os
files=['one.txt','two.txt','three.txt','four.txt','Voweldfsgfg.txt']
os.chdir('D:/Users/pushsing/Desktop/python')
print(os.getcwd())
for i in files:
    try:
        f=open(i,'r+')
        f.write("just opend it second time.")
        print(i)
    except:
        print("File not found")
    else:
        f.close()
        print(i,' closed')
