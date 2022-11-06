fname = input("Enter file name: ")
fh = open(fname)
fmode = input("Press and enter 'S' for Silent mode and 'N' for normal mode: ")


if fmode == 'S':
    print("The process has been completed in silent mode.")

elif fmode == 'N':
    for i in fh:
        i = i.rstrip().upper()
        print(i)
    print("The process has been completed in normal mode.")

else:
       print("Please enter a valid option.")

