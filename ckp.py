filename = input("path:  \n")
flag = input("Silent Mode: Y/N:  \n")
f = open(filename)

n = 1

if flag == "Y":
    for line in f:
        print (n, line)
        i = i+1

elif flag =="N":
    for line in f:
        input("Continue")
        print(i, line)
        i = i+1
        f.close()